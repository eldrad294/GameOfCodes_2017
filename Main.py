import InputHandler as ih
import OutputHandler as oh
import Utils as util
import Constants as const
#
# Writes over and creates new route_file.rd
oh.clear_data_in_file()
#
# Reads from roads_file.rds
inward = ih.read_data(const.ROADS_FILE_PATH)
#
# We order road_timings by order asc of start location
ordered_road_timings = util.order_by_start(inward.start_loc, inward.get_road_timings())
# for road_timing in inward.get_road_timings:
#     print(road_timing.start)
#
# Vars
timer = 0
#
for road_timing in ordered_road_timings:
    #
    oh.write_data(road_timing.destination)
    if inward.end_loc == road_timing.destination:
        pass
#
print(timer)