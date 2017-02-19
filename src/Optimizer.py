import src.Constants as const
#
def get_optimizer_results(all_timings, all_routes):
    equal_timings = []
    equal_routes = []
    for i, timing in enumerate(all_timings):
        if min(all_timings) == timing:
            equal_timings.append(timing)
            equal_routes.append(all_routes[i])
    if len(equal_timings) == 1:
        #
        # If this is the single most optimize route, we return it
        return equal_routes[0]
    else:
        #
        # Removing coffee stops when comparing final paths
        paths_without_coffees = []
        paths_with_coffees = []
        for routes in equal_routes:
            path_without = []
            path_with = []
            for route in routes:
                if const.COFFEE in route:
                    path_with.append(route)
                else:
                    path_without.append(route)
            paths_without_coffees.append(path_without)
            paths_with_coffees.append(path_with)
        #
        # Checking length of route stops now that we separated coffee stops from actual routes
        index = []
        min_value = 10000
        for i, path_without in enumerate(paths_with_coffees):
            if len(index) == 0 or len(path_without) <= min_value:
                index.append(i)
                min_value = len(path_without)
        #
        if len(index) == 1:
            return all_routes[index[0]]
        else:
            #
            # If non-coffee routes are not enough to break a tie, we calculate total number of coffee stops
            index = 0
            total_coffee = 0
            for i, paths in enumerate(paths_with_coffees):
                if total_coffee < coffee_timer(paths):
                    index = i
            return all_routes[index], equal_timings[index]
            # optimized_timing = all_timings.index(min(all_timings))
            # return all_routes[optimized_timing]
#
def coffee_timer(routes):
    total = 0
    for route in routes:
        if const.COFFEE in route:
            total += int(route.split(" ")[1])
    return total
