# Flight Efficiency Assessment with ICAO KPIs

Introduction
The aim of this project is to develop and provide some key performance indicators(KPI) proposed
by ICAO to measure ATM performance according to https://www4.icao.int/ganpportal/ASBU/KPI by means of a data analysis code that parses the given DDR2 air traffic data provided by Eurocontrol which contains the historical flight data in Europe.
The scope of data analysis has been chosen in the date of July 24, 2016. The raw data that has been
provided are two text based data files in .so6 format. The first file is the M1 file that contains
the filed flight plans, and the second file is the M2 which contains the actual flown trajectories

Data analysis process
The strategy followed to carry out this project is very similar to that of the data analysis process.
The whole process is in fact aimed to gather and process raw data, explore it and analyze the
information to give conclusions.
The chosen programming language is Python v3.9.7 with various libraries included such as:
• pandas: It is a library for data management and analysis using flexible and expressive data
structures. In this project the used data structure for data analysis will be the dataFrame
which groups all values on a table in which can be applied various methods and functions.
• matplotlib: It is a library for creating visualizations and graphs from data
• geopy: It is a library that helps to locate coordinates of cities, countries and landmarks across
the globe
• math: A library used for the purpose of mathematical operations with additional functions
• geographiclib: It is a library that helps to calculate geodesic and rhumb line calculations such
as great circle distance(GCD).
The full code implementations is modular and composed of various additional functions that are
necessary to calculate certain parameters as it will be requested.




