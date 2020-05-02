from floodsystem.stationdata import build_station_list , update_water_levels
from floodsystem.station import MonitoringStation
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import update_water_levels
from analysis import polyfit
from flood import stations_highest_rel_level


def plot_water_level_with_fit1(station,dates, levels, p):

    if type(p) != int:
        assert ValueError("p must be an integar")
    
    
    x = matplotlib.dates.date2num(dates)
    y = levels
    
    p_coeff = np.polyfit(x, y, p)
    
    poly = np.poly1d(p_coeff)
    
    plt.plot(x, y, label = "water levels")
    typical_range = station.typical_range
    
    x1 = np.linspace(x[0], x[-1], len(x))
    low_levels = [typical_range[0]]*len(dates)
    high_levels = [typical_range[1]]*len(dates)

    plt.plot(dates,low_levels, label = "low range")
    plt.plot(dates,high_levels, label = "high range")  

    

    
    plt.plot(x1, poly(x1), label = "least squares line")
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.legend()
    plt.show()



def run():

    stations = build_station_list()
    update_water_levels(stations)
    
    water_levels = []
    water_levels = stations_highest_rel_level(stations,5)
    
    dt = 2
    
    for monitoring_station in water_levels:
        dates, levels = fetch_measure_levels(monitoring_station[0].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit1(monitoring_station[0],dates,levels,5)



if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()







