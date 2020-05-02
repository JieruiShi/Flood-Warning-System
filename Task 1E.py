from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    N = 10
    """choose to show the first N number of rivers with the highest number of stations"""
    rivers = rivers_by_station_number(stations,N)

    print(rivers)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()


