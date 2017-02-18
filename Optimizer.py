def get_optimizer_results(all_timings, all_routes):
    optimized_timing = all_timings.index(max(all_timings))
    return all_routes[optimized_timing]