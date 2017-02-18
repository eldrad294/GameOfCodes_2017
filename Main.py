import InputHandler as ih
import OutputHandler as oh
import Utils as util
import Constants as const
import concurrent.futures as cf
import Optimizer as o
#
# Writes over and creates new route_file.rd
oh.clear_data_in_file()
#
# Reads from roads_file.rds
inward = ih.read_data(const.ROADS_FILE_PATH)
#
# We order road_timings by order asc of start location
# ordered_road_timings = util.order_by_start(inward.start_loc, inward.get_road_timings())
# for road_timing in ordered_road_timings:
#     print(road_timing.start)
#
with cf.ThreadPoolExecutor(max_workers=4) as executor:
    #
    # Kicking off 4 simultaneous jobs
    thread1 = executor.submit(util.route_finder, inward, timer=0, patience_level=2, current_loc='start')
    thread2 = executor.submit(util.route_finder, inward, timer=0, patience_level=2, current_loc='start')
    thread3 = executor.submit(util.route_finder, inward, timer=0, patience_level=2, current_loc='start')
    thread4 = executor.submit(util.route_finder, inward, timer=0, patience_level=2, current_loc='start')
    #
    timer1, route_list_1 = thread1.result()
    timer2, route_list_2 = thread2.result()
    timer3, route_list_3 = thread3.result()
    timer4, route_list_4 = thread4.result()
#
all_timings = []
all_timings.append(timer1)
all_timings.append(timer2)
all_timings.append(timer3)
all_timings.append(timer4)
#
all_routes = []
all_routes.append(route_list_1)
all_routes.append(route_list_2)
all_routes.append(route_list_3)
all_routes.append(route_list_4)
#
# Calling the optimizer method to decide which was the fastest route and writing  contents of routes to rd file
routes, timing = o.get_optimizer_results(all_timings, all_routes)
for route in routes:
    oh.write_data(route)
    print(timing)
    exit(1)
#
# ret, route_file_list = util.route_finder(
#     inward=inward,
#     timer=timer,
#     patience_level=patience_level,
#     current_loc=current_loc)
# print(route_file_list, ret)