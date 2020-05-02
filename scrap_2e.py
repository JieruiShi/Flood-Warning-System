from plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.station import MonitoringStation
import matplotlib.pyplot as plt
from floodsystem.utils import sorted_by_key
from floodsystem.geo import 


def plot_water_levels1(station, dates, levels):

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

stations = build_station_list()

 