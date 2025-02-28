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




