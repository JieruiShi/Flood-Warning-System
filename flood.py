def stations_level_over_threshold(stations, tol):
    """Takes in a list of monitoring station objects, returns a list of tuples that contain the station and relative
    water level, sorted by the relative water level"""
    newlist = []
    for station in stations:
        if station.relative_water_level() != None and station.relative_water_level() > tol:
            newlist.append((station,station.relative_water_level()))
    return sorted(newlist, key = lambda tup:tup[1], reverse = True)

def stations_highest_rel_level(stations, N):
    """Takes in a list of monitoring station objects and return a list of tuples of (station, relative water level) with the
    highest relative water level"""
    newlist = []
    for station in stations:
        if station.relative_water_level() != None:
            newlist.append((station,station.relative_water_level()))
    if N > len(newlist):
        raise ValueError("N is larger than the amount of stations that gives consistent relative water level")
    else:
        sortedlist = sorted(newlist, key = lambda tup:tup[1], reverse = True)
        finallist = []
        for n in range(N):
            finallist.append(sortedlist[n])
    return finallist


