import math as math

def get_point(lat1,lon1,dist,brng):
    R=3440.1
    lat1=math.radians(lat1)
    lon1=math.radians(lon1)
    lat=math.asin(math.sin(lat1)*math.cos(dist/R)+math.cos(lat1)*math.sin(dist/R)*math.cos(brng))
    lon=lon1 + math.atan2(math.sin(brng)*math.sin(dist/R)*math.cos(lat1),math.cos(dist/R)-math.sin(lat1)*math.sin(lat))
    P=(lat*180/math.pi,lon*180/math.pi)
    return P