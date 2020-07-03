# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

# local = LatLon( 1, 2)
# print(local.lat, local.lon)
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        LatLon.__init__(self,lat,lon)
        self.name = name
    def __str__(self):
        return f"Name:{self.name}, Latitude: {self.lat}, Longitude: {self.lon}"

# local2 = Waypoint(1,2,"jim")
# print(local2.lat, local2.lon, local2.name)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        Waypoint.__init__(self, lat, lon, name)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        inherit = Waypoint.__str__(self)
        current = f", Difficult: {self.difficulty}, Size: {self.size}"
        return inherit + current
# local3 = Geocache(1,2,"jim",10,200)
# print(local3.lat, local3.lon, local3.name, local3.difficulty, local3.size)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint(41.70505,-121.51521,"Catacombs")
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(44.052137,-121.41556,"Newberry Views", 1.5, 2)
# Print it--also make this print more nicely
print(geocache)
