import Constants as const
#
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
#
def look_ahead_for_coffee(timer, patience_level, road_timing):
    """ Coffee  look ahead for current level 0 route """
    for i, timing in enumerate(road_timing[timer:]):
        timing = int(timing)
        if timing <= patience_level:
            return i
#
def route_finder(inward, timer, patience_level, current_loc, road_timings):
    """ This function provides the optimum path with least timing possible """
    route_file_list = []
    for j, road_timing in enumerate(road_timings):
        #
        # Var Initialization
        coffee_break = 0
        #
        # Checks if the next locations picked up is where we last left off.
        # This condition is disregarded for first road junction
        if current_loc != road_timing.start and j != 0:
            continue
        #
        # Iterating over road timings of a specific road junction
        for i, time in enumerate(road_timing.get_time()):
            time = int(time)
            if i >= timer:
                #
                # If we don't have patience, lets consider a coffee
                if time > patience_level:
                    #
                    # If the location has a coffee shop, and we haven't had a coffee yet for this stop,
                    # have coffee break
                    if has_coffee(inward.start_loc) and coffee_break == 0:
                        coffee_break = look_ahead_for_coffee(timer, patience_level, road_timing.get_time())
                        #
                        # Advance timer and write to RT file. For the first road iteration, we do not count the
                        # time taken for coffee break
                        if j != 0:
                            timer += coffee_break
                        route_file_list.append(const.COFFEE + " " + str(coffee_break))
                        continue
                #
                timer += time
                route_file_list.append(road_timing.destination)
                #
                break
        #
        if inward.end_loc == road_timing.destination:
            break
        #
        # Assigns the road destination to current_loc variable
        current_loc = road_timing.destination
    return timer, route_file_list

