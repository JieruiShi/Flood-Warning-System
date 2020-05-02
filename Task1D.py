from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station

def run():
    """Requirements for Task 1D"""

    
    
    stations = build_station_list()
    a = rivers_with_station(stations)
    b = sorted(a)
    c = b[:10]
    print("rivers with atleast 1 monitoring station",c)
    print(len(b))


    x = stations_by_river(stations)
    y = x["River Aire"]
    z = sorted(y)
    print("River Aire",z)    


    x1 = stations_by_river(stations)
    y1 = x1["River Cam"]
    z1 = sorted(y1)
    print("River Cam",z1)  

    x2 = stations_by_river(stations)
    y2 = x2["River Thames"]
    z2 = sorted(y2)
    print("River Thames",z2) 







    



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()








