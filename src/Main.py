import src.InputHandler as ih
import src.OutputHandler as oh
import src.Utils as util
import concurrent.futures as cf
import src.Optimizer as o
import sys
#
# Receving Inputs
try:
    ROADS_FILE_PATH = sys.argv[1]
    ROUTE_FILE_PATH = sys.argv[2]
    print("Opening " + ROADS_FILE_PATH)
    print("Opening " + ROUTE_FILE_PATH)
except Exception as e:
    print(str(e))
    exit(1)
#
# Writes over and creates new route_file.rd
oh.clear_data_in_file(ROUTE_FILE_PATH)
#
# Reads from roads_file.rds
inward = ih.read_data(ROADS_FILE_PATH)
#
# We order road_timings by order asc of start location
unordered_road_timings = inward.get_road_timings()
ordered_road_timings = util.order_by_start(inward.start_loc, inward.get_road_timings())
#
with cf.ThreadPoolExecutor(max_workers=4) as executor:
    #
    # Kicking off 4 simultaneous jobs
    thread1 = executor.submit(util.route_finder, inward, timer=0, patience_level=1, current_loc='start', road_timings=unordered_road_timings)
    thread2 = executor.submit(util.route_finder, inward, timer=0, patience_level=2, current_loc='start', road_timings=ordered_road_timings)
    thread3 = executor.submit(util.route_finder, inward, timer=0, patience_level=3, current_loc='start', road_timings=unordered_road_timings)
    thread4 = executor.submit(util.route_finder, inward, timer=0, patience_level=4, current_loc='start', road_timings=ordered_road_timings)
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
    oh.write_data(ROUTE_FILE_PATH, route)
print(timing)
#
# ret, route_file_list = util.route_finder(
#     inward=inward,
#     timer=timer,
#     patience_level=patience_level,
#     current_loc=current_loc)
# print(route_file_list, ret)