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




