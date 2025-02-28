# Flight Efficiency Assessment with ICAO KPIs

## Introduction
The aim of this project is to develop and provide some key performance indicators(KPI) proposed
by ICAO to measure ATM performance according to https://www4.icao.int/ganpportal/ASBU/KPI by means of a data analysis code that parses the given DDR2 air traffic data provided by Eurocontrol at https://www.eurocontrol.int/ddr which contains the historical flight data in Europe. The scope of data analysis has been chosen in the date of July 24, 2016. The raw data contains the filed flight plans and the actual flown trajectories.

## Data analysis process
The chosen programming language is Python v3.9.7 with various libraries included such as pandas, matplotlib, geopy and mathgeographiclib The full implementations is modular and composed of various additional functions that are necessary to calculate certain parameters as it will be requested.

## Data analysis process
The format described by the Demand Data Repository(DDR2) documentation, which
comes from Eurocontrol database for pan-European air traffic describes how the documents must be interpreted, which in this case it is composed of flight trajectories data separated in segments. Therefore, various fields can be read such as flight ID, sequence, times or flight levels.

## Data cleaning
The data is adapted and cleaned from empty values or missing information in the same function as before. It has been observed that around 32 flights plans had been filed but not actually flown, among other issues with the data. Therefore, after cleaning the data, it is ready to be manipulated.

## Analysis and visualization
The final analysis is carried out by comparing the final outputs with the analysis from the given
Eurocontrol Performance Review Reports(PRR) from 2016 and 2017, where they assess the pan-European air traffic by using some of these KPIs.

## Departure punctuality KPI01
This KPI is used to measure the percentage of IFR flights departing from the gate on-time as a
percentage of different variants that correspond to different windows of time and delay of 5 and 15
minutes.

| |ECAC|UK|France|Netherlands|Germany|Spain|
| --- | --- | --- | --- | --- | --- | --- |
|Variant 1A| 39.79| 38.26| 35.14| 38.87| 42.74| 39.8|
|Variant 1B| 23.74| 21.66| 20.86| 24.5| 27| 24.47|
|Variant 2A| 77.47| 74.10| 71.02| 79.51| 81.1| 75.45|
|Variant 2B| 50.79| 46.23| 47.38| 54.77| 58.83| 52.8|

| |EGLL|LFPG|EHAM|EDDF|LEMD|
| --- | --- | --- | --- | --- | --- |
|Variant 1A| 31.56| 30.06| 38.96| 44.57 |53.73|
|Variant 1B| 20.15| 16.57| 24.93| 29.52 |28.92|
|Variant 2A| 64| 60| 79.02| 82.78| 89.37|
|Variant 2B| 47.7| 41.01| 56.13| 63.1 |58.58|


![image](https://github.com/user-attachments/assets/d1e28bd0-c72c-49e4-a2f4-f692dce80780)

![image](https://github.com/user-attachments/assets/12a27472-4a72-461c-a786-938b6b965d82)

![image](https://github.com/user-attachments/assets/794bd31a-39a0-4803-923d-4febc623a394)

The previous figures show that most of the flights are punctual within the time window of 15 minutes, which is the definition of Variant 2A. In case of the other variants, it seems that as the time window for flights is reduced, the less flights are punctual under these constraints. For example, the flights from the most restrictive variant 2B, are punctual with just around 20 % of all scheduled flights in all ECAC airspace. Regarding the derived KPIs for countries and airports, it can be observed that the similar trend applies. On the one hand, it seems that Germany has the best quality in its overall airspace but on the other hand, the best quality can be found in another country which is not Germany but in Spain at the airport of Madrid.

## Filed flight plan en-route extension KPI04
This KPI measures the en-route horizontal flight efficiency contained in a set of filed flight plans crossing an airspace volume measured in percentage of excess distance. In this case, the methodology to calculate the KPI is not going to be the exact method that ICAO proposes. Instead of having a measured and reference areas, all flights are analyzed under the same scope but the 40 NM radius cylinders around the airport are used as observed in the following figure.

![image](https://github.com/user-attachments/assets/56677e0a-d347-43eb-bfb2-57241160f84c)

1. Calculation of all points distances from the origin or departure coordinates of the correspond-
ing airport for each flight with their given latitude/longitude points
2. Classification of the points if they are inside of the 40 NM radius cylinder or not for each
flight.
3. Find the first segment that crosses the cylinder perimeter. This is done by restricting the
first point P1 or P3,for departure or arrival respectively, of any segment to be greater than
40, and the last point of the same segment which could be P2 or P4, to be less than 40.
4. Find the coordinates of point O1 or O2 for departure or arrival respectively. This is done
by calculating the bearing of the previous segment that has been found with the two known
points. Then, with the known distance of the segment inside the cylinder, the new middle
point at the limit of the cylinder.
5. The distance of the GCD route can be calculate between the previously calculated points 01
and 02 for departure and arrival respectively using a geodesic function already implemented.
Then, the total distance of the filed route(or actual route for the next KPI) can be calculated
as well with these points by using the length of the segments. In the code implementation the
full filed flight plan distance has been calculated and then the value of the small parts of the
segments distances that are inside each cylinder have been subtracted as they were known
later.
6. Finally, the value of the KPI can be calculated as the excess distance, which would be the
filed(or actual) distance minus the GCD distance divided by the GCD distance again, and
expressed as a percentage.

$$100*((Distance − GCD distance)/GCD distance)$$

| |ECAC|UK|France|Netherlands|Germany|Spain|
| --- | --- | --- | --- | --- | --- | --- |
|Filed flight plan en-route extension[%] | 9.02 |7.78| 9.5| 7.11| 9.24| 9.98|

| |EGLL|LFPG|EHAM|EDDF|LEMD|
| --- | --- | --- | --- | --- | --- |
|Filed flight plan en-route extension[%] | 5.17 | 6.19 | 6.76 | 7.15 | 7.04|

![image](https://github.com/user-attachments/assets/06e4b669-f5af-4648-9076-173573d280fe)

![image](https://github.com/user-attachments/assets/a779bf71-3de2-4c2e-a9d5-de3fde863ed4)

The final results show that Netherlands has the most efficient use of airspace during flight planning, and Spain the worst. However, when looking at their major airports, it can be found that their efficiency is better, which would mean that each State may prioritize these airports rather than other local ones, as for example Paris airport(LFPG) which efficiency differs around 3% from the country airspace. Also, the threshold line indicates which countries diverge most of the average European airspace which in this case would be France, Germany and Spain. 

## Filed flight plan en-route extension KPI05
This KPI is similar to the previous one, but instead of filed flight plans, it uses the actual flown trajectories data to calculate the excess distance.

| |ECAC|UK|France|Netherlands|Germany|Spain|
| --- | --- | --- | --- | --- | --- | --- |
|Actual trajectory en-route extension[%] | 8.65| 7.82| 9.07| 7.14| 8.73| 9.44|

| |EGLL|LFPG|EHAM|EDDF|LEMD|
| --- | --- | --- | --- | --- | --- |
|Actual trajectory en-route extension[%]| 5.28| 6.2| 6.87| 6.89| 6.86|

![image](https://github.com/user-attachments/assets/3cda4f4a-0bb3-482d-928c-45c51fb16bb9)

![image](https://github.com/user-attachments/assets/39bd9cb9-8991-4a49-9628-cb33fffc9fdf)

The results from the actual trajectories show similar trends as seen before with the flight plans
ones, however it can be found that the efficiency has improved slightly in all the ECAC airspace,
countries and airports if not just maintained. This is a good indicator according to ICAO, which
indicates that there shouldn’t be a big lap between the values of flight plans with the actual
trajectories. Also, they indicate which countries are below the
Eurocontrol area average, which include Spain and France as it can be translated as that Spain
and France are above the average ECAC inefficiencty, therefore having a worse airspace efficiency.

## Arrival punctuality KPI14
The arrival punctuality is very similar to the previous KPI01 counterpart, but with the flights
arriving to its gate at their destination instead.

| |ECAC|UK|France|Netherlands|Germany|Spain|
| --- | --- | --- | --- | --- | --- | --- |
|Variant 1A| 31.65| 27.3| 27.58| 28.64| 34.7| 32.87|
|Variant 1B| 17.53| 15.24| 14.7| 17.09| 19.6| 18.26|
|Variant 2A| 71.76| 64.55| 67.29| 71.29| 74.03| 73.37|
|Variant 2B| 43.42| 41.95| 39.96| 50| 43.88| 45.03|

| |EGLL|LFPG|EHAM|EDDF|LEMD|
| --- | --- | --- | --- | --- | --- |
|Variant 1A| 16.03| 26.14| 28.86| 32.51| 36.78|
|Variant 1B| 10.44| 17.05| 17.18| 20.61| 23|
|Variant 2A| 52.79| 65.48| 71.54| 70.1| 73.75|
|Variant 2B| 43.82| 49.72| 52.48| 48.48| 49.43|

![image](https://github.com/user-attachments/assets/51e238d8-9d62-45b7-be8f-0dab220c3902)

![image](https://github.com/user-attachments/assets/3a8220d2-aceb-4833-af6c-f5a24f609d10)

![image](https://github.com/user-attachments/assets/a4ce01ca-390d-42b3-943c-68262bfff8d4)

The variant 2A is the one with most percentage of punctual flights. This behaviour is also linked to the Eurocontrol reports, which show a similar percentage for the same variant over the past years. In this case, the best quality airport is still Madrid airport and the best airspace quality corresponds to Germany. Regarding the differences between this KPI and its departures counterpart, it can be observed clearly that the punctuality is worse at arrival. According to Eurocontrol, this is because the arrival punctuality is linked to departure delay, which have also their specific KPIs, but that is out of scope for this study.

## Level-off during climb KPI17
This KPI calculates the amount of distance and time that the airplane is in level-flight during climb phase from real IFR flights. Ideally, there should not be level flight during climb because of fuel burn and noise. This KPI requires many inputs and data that is not available, so a coarse approach has been carried out.

![image](https://github.com/user-attachments/assets/17906fb3-cad3-42a1-a0fe-ecfe8b37a21b)

1. Identify which segment has the maximum flight level on its first point for each flight. This
is an easy operation that can be done with pandas package by grouping each flightID and
finding the index of the maximum flight level at FLBegin field.
2. With the maximum value of flight level, find all the corresponding cruise phase. By mergin
both tables, it should be posible to delete the full cruise and descent phases from the dataframe
by creating a mask of NaN values.
3. Calculate the time contribution in minutes that has each segment on the same flight with the
dates difference between the segment beginning and ending points.
4. Calculate the distances from the origin airport for each flight by using their coordinates and
GCD function
5. Separate the level flight segments with their corresponding status equal to 2. Also, apply
the condition that all segments must be inside the analysis radius around the airport of 200
NM as shown in the figure 13 as a visualization. Therefore, the top of climb is the maximum
flight level of the entire route, and as an approximation, the first segment of the cruise phase
is not taken into account even if a small portion falls inside the cylinder it is not calculated
as it can be visualized in 13.
6. Calculate the sum of all segments time and distance contributions for each flight.
7. Finally calculate the total average of all flights for the ECAC area. Repeat for countries
and airports values, possibly by using the same dataFrame values stored from the previous
calculation.



