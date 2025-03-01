from readDDR import readDDR
from KPI01 import KPI01
from KPI_enroute import KPI_enroute
from KPI14 import KPI14
from KPI17 import KPI17
from KPI19 import KPI19
from plotKPI01_14 import plotKPI01_14
from plotKPI04_05 import plotKPI04_05
from plotKPI17_19 import plotKPI17_19

value=input('Enter the number of KPI: ')

[m1,m3]=readDDR() #Read DDR2 files

# Input data to calculate the corresponding derived KPIs
countries_id=['EG','LF','EH','ED','LE']
countries_name=['United Kingdom','France','Netherlands','Germany','Spain']
airports=['EGLL','LFPG','EHAM','EDDF','LEMD']

if(value == '01'):
    KPI_departure_punctuality=KPI01(m1,m3,countries_id,countries_name,airports) # KPI 01
    print(KPI_departure_punctuality)
    plotKPI01_14(KPI_departure_punctuality)

elif(value == '04'):
    KPI_filed_extension=KPI_enroute(m1,countries_id,countries_name,airports) # KPI 04
    print(KPI_filed_extension)
    plotKPI04_05(KPI_filed_extension)

elif(value == '05'):
    KPI_actual_extension=KPI_enroute(m3,countries_id,countries_name,airports) # KPI 05
    print(KPI_actual_extension)
    plotKPI04_05(KPI_actual_extension)

elif(value == '14'):
    KPI_arrival_punctuality=KPI14(m1,m3,countries_id,countries_name,airports) # KPI 14
    print(KPI_arrival_punctuality)
    plotKPI01_14(KPI_arrival_punctuality)

elif(value == '17'):
    KPI_climb=KPI17(m3,countries_id,countries_name,airports) # KPI 17
    print(KPI_climb)
    plotKPI17_19(KPI_climb)

elif(value == '19'):
    KPI_descent=KPI19(m3,countries_id,countries_name,airports) # KPI 19
    print(KPI_descent)
    plotKPI17_19(KPI_descent)

else:
    print("Invalid input")