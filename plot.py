from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import update_water_levels


def plot_water_levels(station, dates, levels):

     if len(dates) != len(levels):
          assert ValueError("The number of data entries for levels must equal entries for dates")

     if type(station) != MonitoringStation:
          assert TypeError("station must be a monitoring station object")

     

     typical_range = station.typical_range
     
     low_levels = [typical_range[0]]*len(dates)
     high_levels = [typical_range[1]]*len(dates)




     
     plt.plot(dates,low_levels, label = "low range")
     plt.plot(dates,high_levels, label = "high range")     
     plt.plot(dates, levels, label = "water levels")




     plt.xlabel('date')
     plt.ylabel('water level (m)')
     plt.xticks(rotation=45)
     plt.title(station.name)
     plt.legend()
     
     plt.tight_layout()  
     
     plt.show()




def plot_water_level_with_fit(station,dates, levels, p):

    if type(p) != int:
        assert ValueError("p must be an integar")
    
    if len(levels) != len(dates):
         assert ValueError("number of entries of levels must equal dates")
    
    x = matplotlib.dates.date2num(dates)
    y = levels
    
    p_coeff = np.polyfit(x, y, p)
    
    poly = np.poly1d(p_coeff)
    
    plt.plot(x, y, label = "water levels")
    
    x1 = np.linspace(x[0], x[-1], len(x))
    
    plt.plot(x1, poly(x1), label = "least squares line")
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.legend()
    plt.show()

stations  = build_station_list()

station_cam = None

for station in stations:
    if station.name == "St Mary Bourne":
        station_test = station





