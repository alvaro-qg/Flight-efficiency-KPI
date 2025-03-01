import pandas as pd
import numpy as np
from geopy.distance import great_circle

def KPI17(m3,countries_id,countries_name,airports):
        #Convert the column of flight levels to float types
        m3['FLBegin']=m3['FLBegin'].astype(float)
        #Search the maximum value of flight level for each flight
        max_fl=m3.loc[m3.groupby('flightID')['FLBegin'].idxmax()]

        #The top of climb can be found at cruise levels just after the climb phase, therefore we delete the rest of values that are not at cruise
        delete_rows = max_fl[max_fl['status'] != '2'].index
        max_fl=max_fl.drop(delete_rows)
        
        #Convert the times and dates to strings, then to datatime types and finally calculate the difference in order to find
        #the time contribution of each segment in the trajectory for each flight
        m3['timeBegin'] = m3["dateBegin"].astype(str) + "" + m3["timeBegin"].astype(str)
        m3['timeEnd'] = m3["dateEnd"].astype(str) + "" + m3["timeEnd"].astype(str)

        m3['timeBegin'] = pd.to_datetime(m3["timeBegin"], format='%y%m%d%H%M%S')
        m3['timeEnd'] = pd.to_datetime(m3['timeEnd'], format ='%y%m%d%H%M%S')

        m3['time'] = (m3['timeEnd']-m3['timeBegin']).dt.total_seconds()/60

        #Data cleaning
        m3=m3.drop(['timeBegin','timeEnd'], axis=1) 
        max_fl=max_fl.drop(['origin','destination','timeBegin','timeEnd','FLBegin','FLEnd','status','dateBegin','dateEnd','latBegin','lonBegin','latEnd','lonEnd'],axis=1)
        
        #We merge the maximum levels of flight to the main dataframe in order to match the segment sequence they are positioned
        m3=m3.merge(max_fl, on=['flightID','sequence'], how='left')
        #Then by using a mask and filling with NaN values, we can filter the data and save the climb phases of each flight only
        mask = m3['segLength_y'].where(m3['segLength_y'].isna() == False).groupby(m3['flightID']).ffill()
        m3= m3[mask.isnull()]

        # Calculation of distances from the origin airport for each coordinate of each segment
        P1=list(zip(m3['latBegin'].astype(float).div(60), m3['lonBegin'].astype(float).div(60)))
        P2=list(zip(m3['latEnd'].astype(float).div(60), m3['lonEnd'].astype(float).div(60)))

        m3['Origin Airport Coords']=P1
        m3['Origin Airport Coords'] = m3.groupby('flightID')['Origin Airport Coords'].transform('first')

        m3['P1 Coords'] = P1
        m3['P2 Coords'] = P2

        m3=m3.drop(['latBegin','lonBegin','latEnd','lonEnd'], axis = 1)

        m3['distanceP1'] = m3.apply (lambda row: great_circle(row['Origin Airport Coords'],row['P1 Coords']).nm, axis=1)
        m3['distanceP2'] = m3.apply (lambda row: great_circle(row['Origin Airport Coords'],row['P2 Coords']).nm, axis=1)

        #Select the rows with level-off status that are inside the radius of study of 200 NM
        m3=m3.loc[(m3['status'] == '2') & (m3['distanceP1']<=200) & (m3['distanceP2']<=200)]
        
        #Convert from string to float types
        m3['segLength_x']=m3['segLength_x'].astype(float)
        m3['time']=m3['time'].astype(float)

        m3['country'] = m3['origin'].str[-4:-2] #Create country column with the destination

        level_off_distances = m3.groupby(['flightID'])['segLength_x'].sum() #Sum lengths to get the level-off distance for each flight
        level_off_distances=level_off_distances.reset_index()
        KPI_distance=level_off_distances['segLength_x'].mean() #Calculate the average distance for all the ECAC airspace

        level_off_time = m3.groupby('flightID')['time'].sum() #Sum times to get the level-off duration for each flight
        level_off_time=level_off_time.reset_index()
        KPI_time=level_off_time['time'].mean() #Calculate the average time for all the ECAC airspace

        KPI_ECAC = [KPI_distance,KPI_time]

        #Loop through all the countries
        KPI_country=[]
        for country in countries_id:
                m_country=m3[m3['country']==country]
                distances_country = m_country.groupby(['flightID'])['segLength_x'].sum()
                distances_country=distances_country.reset_index()
                KPI_distance=distances_country['segLength_x'].mean()

                m_country_time = m_country.groupby('flightID')['time'].sum()
                time_country=m_country_time.reset_index()
                KPI_time=time_country['time'].mean()

                KPI_country.append([KPI_distance,KPI_time])

        #Loop through all the airports
        KPI_airport=[]
        for airport in airports:
                m_airport=m3[m3['origin']==airport]
                distances_airport = m_airport.groupby(['flightID'])['segLength_x'].sum()
                distances_airport=distances_airport.reset_index()
                KPI_distance=distances_airport['segLength_x'].mean()

                m_airport_time = m_airport.groupby('flightID')['time'].sum()
                time_airport=m_airport_time.reset_index()
                KPI_time=time_airport['time'].mean()
                KPI_airport.append([KPI_distance,KPI_time])

        #Create a new dataframe with all the previous KPIs calculations
        Rows=['ECAC',countries_name[0],countries_name[1],countries_name[2],countries_name[3],countries_name[4],airports[0],airports[1],airports[2],airports[3],airports[4]]
        Columns=['Average distance','Average time']

        KPI_climb=pd.DataFrame([KPI_ECAC,KPI_country[0],KPI_country[1],KPI_country[2],KPI_country[3],KPI_country[4],KPI_airport[0],KPI_airport[1],KPI_airport[2],KPI_airport[3],KPI_airport[4]],Rows,Columns)

        return KPI_climb