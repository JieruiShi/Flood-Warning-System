from flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    above_station = stations_highest_rel_level(stations,N)
    for tupledata in above_station:
        print(tupledata[0].name + "  " + str(tupledata[1]))


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()