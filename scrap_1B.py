from math import sqrt
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key
from Haversine_formula import haversine


def stations_by_distance(stations, p):
    if type(p) != tuple:
        raise TypeError("p must be a tuple")
    elif len(p) != 2:
        raise ValueError("Coordinates must have 2 values")
    
    else:
        for station in stations:
            if type(station) != MonitoringStation :
                raise TypeError('stations must be a list of Monitoring station objects')
            else:
                pass
        
        list_of_distance_tuples = []
        for station1 in stations:
            station_coordinates = station1.coord
            distance = haversine(p[1],p[0],station_coordinates[1],station_coordinates[0])
            tuple_of_distance = (station1.name,distance)
            list_of_distance_tuples.append(tuple_of_distance)
    
    sorted_list = sorted_by_key(list_of_distance_tuples,1)
    
    
    return(sorted_list)

stations = build_station_list()
p =(52.2053,0.1218)

a = stations_by_distance(stations,p)

print(a)
            



            






