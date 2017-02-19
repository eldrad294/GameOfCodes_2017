class RoadTimings:
    #
    def __init__(self, start, destination, time):
        self.start = start.strip("\n")
        self.destination = destination.strip("\n")
        self.time = time
        self.time[-1] = self.time[-1].strip("\n")
    #
    def get_time(self):
        return self.time