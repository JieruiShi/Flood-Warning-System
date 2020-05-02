import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates 
from floodsystem.stationdata import build_station_list , update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels




def polyfit(dates, levels, p):

    if type(p) != int:
        assert ValueError("p must be an integar")
    
    
    x = matplotlib.dates.date2num(dates)
    y = levels
    
    if not x:
        print("You fucked up")
        return (lambda x: 0, 0)

    p_coeff = np.polyfit(x, y, p)
    
    poly = np.poly1d(p_coeff)

    shift = x[0] 

    output_tuple = (poly,shift)

    return  output_tuple


stations = build_station_list()

station_cam = None

for station in stations:
    if station.name == "Cam":
        station_cam = station
        break


dt = 2


dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))


polyfit(dates,levels,2)










