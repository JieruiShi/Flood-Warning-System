from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    """requirement for 1F"""
    stations = build_station_list()
    inconsistent_list = inconsistent_typical_range_stations(stations)
    station_names = []
    print(len(inconsistent_list))
    # convert a list of inconsistent station objects to a list of their names
    for n in range (len(inconsistent_list)):
        station_names += [inconsistent_list[n].name]
    station_names = sorted(station_names)
    print(station_names)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()