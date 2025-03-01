import pandas as pd
import numpy as np
from geopy.distance import great_circle

def KPI19(m3,countries_id,countries_name,airports):
        #Convert each column of flight levels to float types
        m3['FLBegin']=m3['FLBegin'].astype(float)
        m3['FLEnd']=m3['FLEnd'].astype(float)

        #Create a mask of NaN values to detect where the cruise phase ends and the climb phase begins
        mask = m3['FLEnd'].where((m3['FLEnd'] - m3['FLBegin'] < 0) & (m3['status']=='1')).groupby(m3['flightID']).ffill()
        m3= m3[mask.notnull()]

        #Then, those values are deleted from the main dataframe, so that we are left with the descent phases for each flight
        delete_rows = m3[m3['status'] == '0'].index
        m3=m3.drop(delete_rows)
        
        #Convert the times and dates to strings, then to datatime types and finally calculate the difference in order to find
        #the time contribution of each segment in the trajectory for each flight
        m3['timeBegin'] = m3["dateBegin"].astype(str) + "" + m3["timeBegin"].astype(str)
        m3['timeEnd'] = m3["dateEnd"].astype(str) + "" + m3["timeEnd"].astype(str)

        m3['timeBegin'] = pd.to_datetime(m3["timeBegin"], format='%y%m%d%H%M%S')
        m3['timeEnd'] = pd.to_datetime(m3['timeEnd'], format ='%y%m%d%H%M%S')

        m3['time'] = (m3['timeEnd']-m3['timeBegin']).dt.total_seconds()/60
        
        m3=m3.drop(['timeBegin','timeEnd'], axis=1) #Data cleaning

        # Calculation of distances from the destination airport for each coordinate of each segment
        P1=list(zip(m3['latBegin'].astype(float).div(60), m3['lonBegin'].astype(float).div(60)))
        P2=list(zip(m3['latEnd'].astype(float).div(60), m3['lonEnd'].astype(float).div(60)))

        m3['Destination Airport Coords']=P2
        m3['Destination Airport Coords'] = m3.groupby('flightID')['Destination Airport Coords'].transform('last')

        m3['P1 Coords'] = P1
        m3['P2 Coords'] = P2

        m3=m3.drop(['latBegin','lonBegin','latEnd','lonEnd'], axis = 1)

        m3['distanceP1'] = m3.apply (lambda row: great_circle(row['Destination Airport Coords'],row['P1 Coords']).nm, axis=1)
        m3['distanceP2'] = m3.apply (lambda row: great_circle(row['Destination Airport Coords'],row['P2 Coords']).nm, axis=1)

        #Select the rows with level-off status that are inside the radius of study of 200 NM
        m3=m3.loc[(m3['status'] == '2') & (m3['distanceP1']<=200) & (m3['distanceP2']<=200)]

        #Convert from string to float types
        m3['segLength']=m3['segLength'].astype(float)
        m3['time']=m3['time'].astype(float)

        #Create country column with the destination
        m3['country'] = m3['destination'].str[-4:-2]

        level_off_distances = m3.groupby(['flightID'])['segLength'].sum() #Sum lengths to get the level-off distance for each flight
        level_off_distances=level_off_distances.reset_index()
        KPI_distance=level_off_distances['segLength'].mean() #Calculate the average distance for all the ECAC airspace

        level_off_time = m3.groupby('flightID')['time'].sum() #Sum times to get the level-off duration for each flight
        level_off_time=level_off_time.reset_index()
        KPI_time=level_off_time['time'].mean() #Calculate the average time for all the ECAC airspace

        KPI_ECAC = list(np.around(np.array([KPI_distance,KPI_time]),2))

        #Loop through all the countries
        KPI_country=[]
        for country in countries_id:
                m_country=m3[m3['country']==country]
                distances_country = m_country.groupby(['flightID'])['segLength'].sum()
                distances_country=distances_country.reset_index()
                KPI_distance=distances_country['segLength'].mean()

                m_country_time = m_country.groupby('flightID')['time'].sum()
                time_country=m_country_time.reset_index()
                KPI_time=time_country['time'].mean()

                KPI_country.append(list(np.around(np.array([KPI_distance,KPI_time]),2)))

        #Loop through all the airports
        KPI_airport=[]
        for airport in airports:
                m_airport=m3[m3['destination']==airport]
                distances_airport = m_airport.groupby(['flightID'])['segLength'].sum()
                distances_airport=distances_airport.reset_index()
                KPI_distance=distances_airport['segLength'].mean()

                m_airport_time = m_airport.groupby('flightID')['time'].sum()
                time_airport=m_airport_time.reset_index()
                KPI_time=time_airport['time'].mean()
                KPI_airport.append(list(np.around(np.array([KPI_distance,KPI_time]),2)))

        #Create a new dataframe with all the previous KPIs calculations
        Rows=['ECAC',countries_name[0],countries_name[1],countries_name[2],countries_name[3],countries_name[4],airports[0],airports[1],airports[2],airports[3],airports[4]]
        Columns=['Average distance','Average time']

        KPI_descent=pd.DataFrame([KPI_ECAC,KPI_country[0],KPI_country[1],KPI_country[2],KPI_country[3],KPI_country[4],KPI_airport[0],KPI_airport[1],KPI_airport[2],KPI_airport[3],KPI_airport[4]],Rows,Columns)

        return KPI_descent