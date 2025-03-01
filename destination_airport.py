from geopy.distance import great_circle
from bearing import bearing
from get_point import get_point

def destination_airport(m1,P1,P2):   
    #Create the column with the origin airport coordinates for each arrival
    m1['Destination Airport Coords']=P2
    m1['Destination Airport Coords'] = m1.groupby('flightID')['Destination Airport Coords'].transform('last')

    #Create the corresponding columns for each coordination points for both points at the beggining and ending of each segment
    m1['P1 Coords'] = P1
    m1['P2 Coords'] = P2

    m1=m1.drop(['latBegin','lonBegin','latEnd','lonEnd'], axis = 1)#Clean data

    #Calcualte all the distances from the destination airport coordinates to each of the other coordiantes points for each different flightID
    m1['distanceP1'] = m1.apply (lambda row: great_circle(row['Destination Airport Coords'],row['P1 Coords']).nm, axis=1)
    m1['distanceP2'] = m1.apply (lambda row: great_circle(row['Destination Airport Coords'],row['P2 Coords']).nm, axis=1)

    #Store all the segments which fulfill the condition that their last ending point is inside the arrival cylinder and their first beggining
    #point is outside or at the perimeter of the arrival cylinder of 40NM radius.
    arrival_cilinder=m1.loc[(m1['distanceP2'] < 40) & (m1['distanceP1'] >= 40)]

    #The small portion distance of the crossing segment that is inside the arrival cilinder is stored in a column 
    arrival_cilinder['x'] = 40-arrival_cilinder['distanceP2']
    #Calculate bearing of each segment with its coordinates points at the beggining and the ending. Then, calculate the point coordinates
    # that is in the segment at the specific distance of 40 NM from its departure airport, in other words at the exact perimeter of the cilinder
    arrival_cilinder['Bearing'] = arrival_cilinder.apply (lambda row: bearing(row['P2 Coords'][0],row['P2 Coords'][1],row['P1 Coords'][0],row['P1 Coords'][1]), axis=1)
    arrival_cilinder['P Cilinder']=arrival_cilinder.apply (lambda row: get_point(row['P2 Coords'][0],row['P2 Coords'][1],40-row['distanceP2'],row['Bearing']), axis=1)
    arrival_cilinder=arrival_cilinder.drop(['distanceP1','distanceP2','Bearing'], axis = 1)
    
    #The dataframe is passed on as an output with all the previous calculated data and cleaned 
    arrival_cilinder=arrival_cilinder.drop(['sequence','segLength','Destination Airport Coords','P1 Coords','P2 Coords'], axis=1)
    arrival_cilinder=arrival_cilinder.rename(columns = {'P Cilinder':'P2 Destination cilinder'})
    
    return arrival_cilinder