from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from Haversine_formula import haversine
from floodsystem.geo import stations_within_radius



def run():
    """Requirements for Task 1C"""

    # Build list of stations
    
    
    stations = build_station_list()
    b= stations_within_radius(stations,(52.2053, 0.1218),10)
    a= []

    for station in b:
        a.append(station.name)
        c = sorted(a)
        
        

    print(c)



if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()