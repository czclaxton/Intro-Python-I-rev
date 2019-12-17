# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def getLatitude(self):
        return(self.lat)

    def getLongitude(self):
        return(self.lon)

        # def __str__(self):
        #     return '{lat: '+ str(self.lat) +', lon: ' + str(self.lon) + '}'
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
        # def __str__(self):
        #     return '{name: ' + self.name + '}'
    def getName(self):
        return(self.name)

    def __str__(self):
        return 'The location name is the {self.name} and is located at a latitude of {self.lat} and a longitude of {self.lon}'.format(self=self)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size
    def getDifficulty(self):
        return(self.difficulty)

    def getSize(self):
        return(self.size)

    def __str__(self):
        return 'The location name is the {self.name} and is located at a latitude of {self.lat} and a longitude of {self.lon}. The difficulty rating is {self.difficulty} and has an estimated size of {self.size}.'.format(self=self)

        # def __str__(self):
        #     return '{difficulty: ' + self.difficulty + ', size: ' + self.size +'}'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint = Waypoint(41.70505, -121.51521, "Catacombs")
print(waypoint.getName(), waypoint.getLatitude(), waypoint.getLongitude())

# waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
# print(waypoint)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)
# print(waypoint.__str__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)
# geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
# print(geocache.__str__())

