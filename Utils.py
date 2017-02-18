def has_coffee(location):
    return True if "*" in location else False
#
def order_by_start(start_loc, road_timings):
    original_list = []
    temp_list = []
    for road_timing in road_timings:
        if road_timing.start == start_loc:
            temp_list.append(road_timing)
        else:
            original_list.append(road_timing)
    #
    return temp_list + original_list
