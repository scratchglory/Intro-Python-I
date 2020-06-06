# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    """ 
        Part of Waypoint. Provides a longitude and latitude location
    """

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


location = LatLon(71, 90)
print(location.lat)
print(location.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)

    def __str__(self):
        return "{}, is located at {}, {}".format(self.name, self.lat, self.lon)


location1 = Waypoint("NAMERzzz", 12, 35)
print(location1.name)
print(location1.lat)
print(location1.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache(Waypoint):
    def __init__(self, difficulty, size, name, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)

    def __str__(self):
        return "It is a {} type of difficulty, with a size of {}, at {} located at {}, {} ".format(self.difficulty, self.size, self.name, self.lon, self.lat)


geocache1 = Geocache("hard", "large", "person", 45, 88)
print("Geocache Difficulty:", geocache1.difficulty)
print("Geocache size:", geocache1.size)
print("Geocache name:", geocache1.name)
print("Geocache lat:", geocache1.lat)
print("Geocache lon:", geocache1.lon)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(1.5, 2, "Newberry Views", 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
