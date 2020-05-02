from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
import matplotlib.pyplot as plt 
import datetime
from floodsystem.datafetcher import fetch_measure_levels



stations = build_station_list()

station_cam = None

for station in stations:
    if station.name == "Cam":
        station_cam = station
        break


dt = 2


dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))



print(levels)
