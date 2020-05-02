from floodsystem import geo
from floodsystem import station
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
#station = stationdata.build_station_list()
import datetime

stations = build_station_list()
update_water_levels(stations)
towns_risk = {}
for station in stations[1000:1200]:
    if station.relative_water_level() == None:
        pass
        #To make sure the station have a valid relative water level data
    elif not(station.town in towns_risk):
        # check if there is already a station recorded for this city
        count = 1
        risk_factor = 0
        if station.relative_water_level() > 0.7:
            #only considered risky when water lever greater than 0.7
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(hours = 30))
            risk_factor += (station.relative_water_level() - 0.7)
            try:
                risk_factor += 3 * (levels[0] - levels[24]) + (levels[0] - levels[96])
            except:
                pass
        if station.relative_water_level() > 1.0:
            risk_factor += (station.relative_water_level() - 1.0)
    else:
        risk_factor = towns_risk[station.town][1] * towns_risk[station.town][0]
        count = towns_risk[station.town][0] + 1
        if station.relative_water_level() > 0.7:
            #only considered risky when water lever greater than 0.7
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
            risk_factor += (station.relative_water_level() - 0.7) + 3 * (levels[0] - levels[24]) + (
            levels[0] - levels[96])
        if station.relative_water_level() > 1.0:
            risk_factor += (station.relative_water_level() - 1.0)

    towns_risk[station.town] = (count,risk_factor/count)

print(towns_risk)
towns_at_risk = []
for town in towns_risk:
    if towns_risk[town][1] > 0.0:
        if towns_risk[town][1] > 1:
            risk_rate = "severe"
        elif towns_risk[town][1] > 0.7:
            risk_rate = "high"
        elif towns_risk[town][1] > 0.4:
            risk_rate = "moderate"
        else:
            risk_rate = "low"
        towns_at_risk.append((town,towns_risk[town][0],towns_risk[town][1], risk_rate))
towns_at_risk = sorted(towns_at_risk, key = lambda tup:tup[2], reverse = True)
print (towns_at_risk)
N = 20
if len(towns_at_risk) >= N:
    print ("The {} most severe towns are:".format(N))
    for n in range(N):
        print(towns_at_risk[n][0])
        print("The severity is {} ".format(towns_at_risk[n][3] + ".  The risk factor is {}".format(towns_at_risk[n][2])))
else:
    raise ValueError("N is larger than stations that have risk of flooding!")


#print (towns_risk["Little Rissington"][1])
#risk_factor = towns_risk["Little Rissington"][1] * towns_risk["Little Rissington"][0]
#print(risk_factor)

"""
for town in towns[0:5]:
    station_count = 0
    risk_factor = 0
    for station in stations:
        if station.town == town:
            if station.relative_water_level() != None:
                dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = 2))
                station_count += 1
                if station.relative_water_level() > 0.7:
                    risk_factor += (station.relative_water_level()-0.7) + 3*(levels[0]-levels[24]) + (levels[0]-levels[96])
                    if station.relative_water_level() > 1.0:
                        risk_factor += (station.relative_water_level()-1.0)
    if station_count == 0:
        town_risk.append((town,None))
    else:
        town_risk.append((town,risk_factor/station_count))



print(town_risk[0:5])
"""
"""
stationSwindon = None
station_name = "Swindon"
for station in stations:
    if station.town == station_name:
        stationSwindon = station
        break
print (stationSwindon)
print (stationSwindon.relative_water_level())
dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
print (3 * (levels[0] - levels[24]) + (levels[0] - levels[96]))
"""


#print(len(towns))
#print (stations[0])
#print (towns[0])




"""
station_name = "St Mary Bourne"

    # Find station
station_cam = None
stations = build_station_list()
for station in stations:
    if station.name == station_name:
        station_cam = station
        break
dates, levels = fetch_measure_levels(station_cam.measure_id, dt = datetime.timedelta(days = 2))
print (dates)
print (levels)
print (station)
"""