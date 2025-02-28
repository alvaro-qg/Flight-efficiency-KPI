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
|Variant 2A| 64| 60 79.02| 82.78| 89.37|
|Variant 2B| 47.7| 41.01| 56.13| 63.1 |58.58|


![image](https://github.com/user-attachments/assets/d1e28bd0-c72c-49e4-a2f4-f692dce80780)

![image](https://github.com/user-attachments/assets/12a27472-4a72-461c-a786-938b6b965d82)

![image](https://github.com/user-attachments/assets/794bd31a-39a0-4803-923d-4febc623a394)

The previous figures show that most of the flights are punctual within the time window of 15 minutes, which is the definition of Variant 2A. In case of the other variants, it seems that as the time window for flights is reduced, the less flights are punctual under these constraints. For example, the flights from the most restrictive variant 2B, are punctual with just around 20 % of all scheduled flights in all ECAC airspace. Regarding the derived KPIs for countries and airports, it can be observed that the similar trend applies. On the one hand, it seems that Germany has the best quality in its overall airspace but on the other hand, the best quality can be found in another country which is not Germany but in Spain at the airport of Madrid.

## Filed flight plan en-route extension KPI04
This KPI measures the en-route horizontal flight efficiency contained in a set of filed flight plans
crossing an airspace volume. It is measured in percentage of excess distance.












