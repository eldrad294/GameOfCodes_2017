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
patience_level = 2
current_loc = 'start'

#
for j, road_timing in enumerate(ordered_road_timings):
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
            if time >= patience_level:
                #
                # If the location has a coffee shop, and we haven't had a coffee yet for this stop, have coffee break
                if util.has_coffee(inward.start_loc) and coffee_break == 0:
                    coffee_break = 1
                    #coffee_break = util.look_ahead(timer, patience_level, road_timing)
            #
            # Advance timer and write to RT file
            if coffee_break == 0:
                timer += time
                oh.write_data(road_timing.destination)
            else:
                timer += coffee_break
                oh.write_data(const.COFFEE + " " + str(coffee_break))
            break
    #
    if inward.end_loc == road_timing.destination:
        break
    #
    # Assigns the road destination to current_loc variable
    current_loc = road_timing.destination
#
print(timer)