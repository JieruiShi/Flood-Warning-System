from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

stations = build_station_list()

river_stations_dict = {}

for station1 in stations:
    if station1.river not in river_stations_dict.keys():
        a = station1.river
        list_of_stations_on_river = []
        for station2 in stations:
            if  station2.river in [a]:
                list_of_stations_on_river.append(station2.name)
        river_stations_dict[a] = list_of_stations_on_river
    else:
        pass

river_test = river_stations_dict["River Mersey"]

print(river_test)

    