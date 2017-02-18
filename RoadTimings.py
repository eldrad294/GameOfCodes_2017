class RoadTimings:
    #
    def __init__(self, start, destination, time):
        self.start = start.strip("\n")
        self.destination = destination.strip("\n")
        self.time = time
    #
    def get_time(self):
        return self.time