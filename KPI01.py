import pandas as pd
import numpy as np
from sum_variants import sum_variants

def KPI01(m1,m3,countries_id,countries_name,airports):
    #Create two different datafrmes for scheduled departures and actual departures. They are grouped by each flight ID, which is unique
    #for each flight. Also, the origin airport and the time where the flight starts are kept
    scheduledDepartureTime=m1.groupby(['flightID']).agg({'timeBegin': 'first', 'dateBegin':'first','origin': 'first'})
    actualDepartureTime=m3.groupby(['flightID']).agg({'timeBegin': 'first', 'dateBegin':'first','origin': 'first'})

    #Merging the previous dataframes, we can obtain the full table to work with the departures times
    DepartureTime=actualDepartureTime.merge(scheduledDepartureTime, on=['origin','flightID'], how='inner')

    #Renaming the fields of the table    
    DepartureTime.columns = ['ActualTime1','ActualTime2','origin','ScheduledTime1','ScheduledTime2']
    nFlights=DepartureTime.shape[0] #Number of flights is the number of rows of the table

    #Joining all time and date columns of strings
    DepartureTime['ActualDate'] = DepartureTime["ActualTime2"].astype(str) + "" + DepartureTime["ActualTime1"].astype(str)
    DepartureTime['ScheduledDate'] = DepartureTime["ScheduledTime2"].astype(str) + "" + DepartureTime["ScheduledTime1"].astype(str)

    #Calculating the time difference between the actual and scheduled times
    DepartureTime['ActualDate'] = pd.to_datetime(DepartureTime["ActualDate"], format='%y%m%d%H%M%S') #Trnsforming strings to datetime with a given format
    DepartureTime['ScheduledDate'] = pd.to_datetime(DepartureTime['ScheduledDate'], format ='%y%m%d%H%M%S')

    DepartureTime['Time difference'] = (DepartureTime['ActualDate']-DepartureTime['ScheduledDate']).dt.total_seconds()/60

    #Creating an additional column for countries with the first two letter of origin airports
    DepartureTime['country'] = DepartureTime['origin'].str[-4:-2]
    
    TimeDiff=DepartureTime['Time difference'].tolist() #Transforming data to be passoed on to the function

    var1=sum_variants(TimeDiff,nFlights) #This function calculates all the variants with the given list of times and number of flights
    KPI_ECAC = list(np.around(np.array(var1),2)) #Limit number of decimals to 2.

    # Loop through all the given countries to calculate their KPIs
    KPI_country=[]
    for country in countries_id:
        DepartureTimeCountry=DepartureTime[DepartureTime['country']==country]
        TimeDiff=DepartureTimeCountry['Time difference'].tolist()
        nFlights=DepartureTimeCountry.shape[0]
        var2=sum_variants(TimeDiff,nFlights)
        KPI_country.append(list(np.around(np.array(var2),2)))

    # Loop through all the given airports to calculate their KPIs
    KPI_airport=[]
    for airport in airports:
        DepartureTimeAirport=DepartureTime[DepartureTime['origin']==airport]
        TimeDiff=DepartureTimeAirport['Time difference'].tolist()
        nFlights=DepartureTimeAirport.shape[0]
        var3=sum_variants(TimeDiff,nFlights)
        KPI_airport.append(list(np.around(np.array(var3),2)))
    
    #Creating a new dataframe to be passed on as an output
    Rows=['ECAC',countries_name[0],countries_name[1],countries_name[2],countries_name[3],countries_name[4],airports[0],airports[1],airports[2],airports[3],airports[4]]
    Columns=['Variant 1A','Variant 1B', 'Variant 2A', 'Variant 2B']

    KPI_departure_punctuality=pd.DataFrame([KPI_ECAC,KPI_country[0],KPI_country[1],KPI_country[2],KPI_country[3],KPI_country[4],KPI_airport[0],KPI_airport[1],KPI_airport[2],KPI_airport[3],KPI_airport[4]],Rows,Columns)

    return KPI_departure_punctuality