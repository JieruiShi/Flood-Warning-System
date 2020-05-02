from floodsystem.stationdata import build_station_list , update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import sorted_by_key
from plot import plot_water_levels


stations = build_station_list()
station_cam = None

for station in stations:
    if station.name == "Cam":
        station_cam = station


dt = 2
dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))

plot_water_levels(station_cam,dates,levels)




