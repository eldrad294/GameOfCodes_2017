from src.Rds import RDs as rd
from src.RoadTimings import RoadTimings as RT
#
def read_data(filename):
    #
    with open(filename, encoding='ISO-8859-1') as f:
        content = f.readlines()
    #
    road_timings = []
    for c in content[4:]:
        temp_list = c.split(",")
        road_timing = RT(temp_list[0], temp_list[1], temp_list[2:])
        road_timings.append(road_timing)
    #
    return rd(content[0].split(","), content[1], content[2], content[3], road_timings)