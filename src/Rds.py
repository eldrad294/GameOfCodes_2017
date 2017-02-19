class RDs:
    #
    def __init__(self, road_junctions,  start_loc, end_loc, max_time, road_timings):
        self.road_junctions = road_junctions
        self.start_loc = start_loc.strip("\n")
        self.end_loc = end_loc.strip("\n")
        self.max_time = max_time.strip("\n")
        self.road_timings = road_timings
    #
    def get_road_junctions(self):
        return self.road_junctions
    #
    def get_road_timings(self):
        return self.road_timings