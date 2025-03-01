import pandas as pd


def readDDR():
    # Read both filed and actual trajectory files as .csv formatting 
    m1=pd.read_csv("20160724_Initial_ECAC_0000-24H.so6", sep=" ", header=None, dtype = str)
    m3=pd.read_csv("20160724_Actual_ECAC_0000-24H.so6", sep= " ", header=None, dtype = str)

    #Define the DDR2 .so6 fields specified
    fields=['segID', 'origin', 'destination', 'aircraftType', 'timeBegin', 'timeEnd', 'FLBegin', 'FLEnd',
        'status', 'callsign', 'dateBegin', 'dateEnd', 'latBegin', 'lonBegin', 'latEnd', 'lonEnd', 'flightID', 'sequence', 'segLength', 'segParity']

    m1.columns = fields;m3.columns = fields

    #Delete the fields that are not used in the whole project
    m1=m1.drop(['segID','aircraftType','callsign','segParity'], axis=1)
    m3=m3.drop(['segID','aircraftType','callsign','segParity'], axis=1)

    #Data cleaning. Fiind all the flights that have not the corresponding match between filed and actual files
    m11=m1.groupby(['flightID']).last()
    m33=m3.groupby(['flightID']).last()

    m= (m11.merge(m33, on='flightID', how='outer', indicator=True).query('_merge != "both"').drop('_merge', 1))
    m=m.reset_index()
    list_of_flights = m['flightID'].to_list()

    m1 = m1[~m1['flightID'].isin(list_of_flights)]
    m3 = m3[~m3['flightID'].isin(list_of_flights)]

    # Pass on the corresponding dataframes prepared to be managed
    return [m1,m3]
