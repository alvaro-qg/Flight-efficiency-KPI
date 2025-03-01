from geographiclib.geodesic import Geodesic
import math as math

def bearing(lat1,lon1,lat2,lon2):
    brng = Geodesic.WGS84.Inverse(lat1, lon1, lat2, lon2)['azi1']
    return (math.radians(brng))
