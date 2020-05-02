from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from Haversine_formula import haversine




def stations_within_radius(stations, centre, r):
    for station in stations:
            if type(station) != MonitoringStation :
                raise TypeError('stations must be a list of Monitoring station objects')
            else:
                pass

    list_of_stations_within_radius = []

    for station1 in stations:
        station_coordinates = station1.coord
        distance = haversine(centre[1],centre[0],station_coordinates[1],station_coordinates[0])
        if distance < r: 
            list_of_stations_within_radius.append(station1)
        else:
            pass
    
    return(list_of_stations_within_radius)


stations = build_station_list()

centre = (52.2053, 0.1218)
r = 10
a = stations_within_radius(stations,centre,r)

list_of_stations =[]

for station in a:
    list_of_stations.append(station.name)

b = sorted(list_of_stations)

print(b)

    

            
    
