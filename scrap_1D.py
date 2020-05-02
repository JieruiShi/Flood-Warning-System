from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def rivers_with_station(stations):
    set_of_rivers = set()

    for station in stations:
        if type(station) != MonitoringStation :
            raise TypeError('Argument must be a list of Monitoring station objects')
        else :
            set_of_rivers.add(station.river)

    return(set_of_rivers)


stations = build_station_list()

print(rivers_with_station(stations))