from math import sqrt
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key
from Haversine_formula import haversine
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    
    
    stations = build_station_list()
    station_tuple = stations_by_distance(stations,(52.2053, 0.1218))

    a = []
    for n in station_tuple:
        a += [(n[0].name,n[0].town, n[1])]

    c = a[:10]
    d = a[-10:]
        
        

    print("10 closest from cambridge",c)
    print("10 furthest from cambridge",d)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()