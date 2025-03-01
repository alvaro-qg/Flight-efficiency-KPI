import pandas as pd
from origin_airport import origin_airport 
from destination_airport import destination_airport
from geopy.distance import great_circle

def KPI_enroute(m,countries_id,countries_name,airports):
    
    P1=list(zip(m['latBegin'].astype(float).div(60), m['lonBegin'].astype(float).div(60))) #Transform segments beginning points to minutes
    P2=list(zip(m['latEnd'].astype(float).div(60), m['lonEnd'].astype(float).div(60))) #Transform segments ending points to minutes

    departure_cilinder=origin_airport(m,P1,P2) #Creates a dataframe with distances and segments out of the departure cilinder
    arrival_cilinder=destination_airport(m,P1,P2) #Creates a dataframe with distances and segments out of the arrival cilinder
    
    Enroute_distance=departure_cilinder.merge(arrival_cilinder, on=['flightID'], how='inner') #Merges both dataframes to calculate the final total distances

    #Calculation of the GCD with geopy function, and the planned/actual distance where distance + x coressponds to the distance from the first point at the cilinder perimeter
    #to the point of the arrival airport. The x is the value of the small distance portion of the crossing segment at the arrival cilinder. Therefore, by substracting them, we can obtain
    #the total distance without the small portions inside both departure and arrival cilinders crossing segments of 40 NM and for each flight ID. 
    Enroute_distance['GCD'] = Enroute_distance.apply (lambda row: great_circle((row['P1 Departure cilinder'][0],row['P1 Departure cilinder'][1]),(row['P2 Destination cilinder'][0],row['P2 Destination cilinder'][1])).nm, axis=1)
    Enroute_distance['planned/actual distance'] = Enroute_distance['distance + x'] - Enroute_distance['x']

    #Create columns of origin and destination countries
    Enroute_distance['country or'] = Enroute_distance['origin_x'].str[-4:-2]
    Enroute_distance['country des'] = Enroute_distance['destination_x'].str[-4:-2]

    #Calculate the total distances sum of all flights and the corresponding KPI for the ECAC airspace
    total_gcd = Enroute_distance['GCD'].sum()
    total_distance = Enroute_distance['planned/actual distance'].sum()
    KPI_ECAC=100*(total_distance-total_gcd)/total_gcd

    #Loop through each country
    KPI_country=[]
    for country in countries_id:
        enroute_country=Enroute_distance[(Enroute_distance['country or']==country) | (Enroute_distance['country des']==country)]
        country_gcd=enroute_country['GCD'].sum()
        total_distance_country=enroute_country['planned/actual distance'].sum()
        inefficiency_country=100*(total_distance_country-country_gcd)/country_gcd
        KPI_country.append(inefficiency_country)

    #Loop through each airport
    KPI_airport=[]
    for airport in airports:
        enroute_airport=Enroute_distance[(Enroute_distance['origin_x']==airport) | (Enroute_distance['destination_x']==airport)]
        airport_gcd=enroute_airport['GCD'].sum()
        total_distance_airport=enroute_airport['planned/actual distance'].sum()
        inefficiency_airport=100*(total_distance_airport-airport_gcd)/airport_gcd
        KPI_airport.append(inefficiency_airport)

    #Create a new dataframe as an output for all the values
    Rows=['ECAC',countries_name[0],countries_name[1],countries_name[2],countries_name[3],countries_name[4],airports[0],airports[1],airports[2],airports[3],airports[4]]
    Columns=['En-route extension']

    KPI_enroute_inefficiency=pd.DataFrame([KPI_ECAC,KPI_country[0],KPI_country[1],KPI_country[2],KPI_country[3],KPI_country[4],KPI_airport[0],KPI_airport[1],KPI_airport[2],KPI_airport[3],KPI_airport[4]],Rows,Columns)

    return KPI_enroute_inefficiency
