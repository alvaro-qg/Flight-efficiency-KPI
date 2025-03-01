from geopy.distance import great_circle
from bearing import bearing
from get_point import get_point

def origin_airport(m1,P1,P2):   
    #Create the column with the origin airport coordinates for each departure
    m1['Origin Airport Coords']=P1
    m1['Origin Airport Coords'] = m1.groupby('flightID')['Origin Airport Coords'].transform('first')

    #Create the corresponding columns for each coordination points for both points at the beggining and ending of each segment
    m1['P1 Coords'] = P1
    m1['P2 Coords'] = P2

    m1=m1.drop(['latBegin','lonBegin','latEnd','lonEnd'], axis = 1) #Clean data

    #Calcualte all the distances from the origin airport coordinates to each of the other coordiantes points for each different flightID
    m1['distanceP1'] = m1.apply (lambda row: great_circle(row['Origin Airport Coords'],row['P1 Coords']).nm, axis=1)
    m1['distanceP2'] = m1.apply (lambda row: great_circle(row['Origin Airport Coords'],row['P2 Coords']).nm, axis=1)

    #Store all the segments which fulfill the condition that their first begining point is inside the departure cylinder and their last ending point
    # is outside or at the perimiter of the cilinder of 40 NM 
    departure_cilinder=m1.loc[(m1['distanceP1'] < 40) & (m1['distanceP2'] >= 40)]

    departure_cilinder['Segment inside cilinder'] = 40-departure_cilinder['distanceP1'] #Calculate the small portion of each segment that is inside the cilinder

    #Calculate bearing of each segment with its coordinates points at the beggining and the ending. Then, calculate the point coordinates
    # that is in the segment at the specific distance of 40 NM from its origin airport, in other words at the exact perimeter of the cilinder
    departure_cilinder['Bearing'] = departure_cilinder.apply (lambda row: bearing(row['P1 Coords'][0],row['P1 Coords'][1],row['P2 Coords'][0],row['P2 Coords'][1]), axis=1)
    departure_cilinder['P Cilinder']=departure_cilinder.apply (lambda row: get_point(row['P1 Coords'][0],row['P1 Coords'][1],40-row['distanceP1'],row['Bearing']), axis=1)
    departure_cilinder=departure_cilinder.drop(['distanceP1','distanceP2','Bearing'], axis = 1)

    #Merge both tables
    m1=m1.merge(departure_cilinder, on=['flightID','sequence'], how='left')
    
    #Create a mask in order to detect the specific segment that crosses the cilinder. Therefore, by creating NaN values on the first rows that are inside the cilinder,
    #we can filter the actual segments that will contribute to the total distance calculation of the flight
    mask = m1['segLength_y'].where(m1['segLength_y'].isna() == False).groupby(m1['flightID']).ffill()
    m1= m1[mask.notnull()]

    #Finally by substracting the small portion from the total distance of the crossing segments of each flight, we can obtain the real 
    # distance that will be used
    m1['segLength_x']=m1['segLength_x'].astype(float)-m1['Segment inside cilinder'].fillna(0)
    #Data cleaning
    m1=m1.drop(['segLength_y','Origin Airport Coords_y','P1 Coords_y','P2 Coords_y','Segment inside cilinder','P Cilinder'],axis=1)
    #Calculate the distances for each flight Note: These distances are still not the distances used by the KPI because they still have 
    # the small distance portions at the arrival, which will be substracted later.
    m1=m1.groupby(['flightID'])['segLength_x'].sum()
    departure_cilinder=departure_cilinder.merge(m1, on=['flightID'], how='left')
    #The dataframe is passed on as an output with all the previous calculated data and cleaned 
    departure_cilinder=departure_cilinder.drop(['sequence','segLength','Origin Airport Coords','P1 Coords','P2 Coords','Segment inside cilinder'], axis=1)
    departure_cilinder=departure_cilinder.rename(columns = {'P Cilinder':'P1 Departure cilinder', 'segLength_x':'distance + x'})

    return departure_cilinder
    