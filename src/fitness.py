def calculate_fitness(route, map_data):
    distance = sum([map_data[route.route[i]][route.route[i+1]]["distance"] for i in range(len(route.route)-1)])
    priority = sum([map_data[point]["priority"] for point in route.route])
    accessibility = sum([map_data[point]["accessibility"] for point in route.route])
    waiting_time = sum([map_data[point]["waiting_time"] for point in route.route])
    logistic_cost = sum([map_data[point]["cost"] for point in route.route])

    fitness = (1 / (distance + 1)) + priority + accessibility - waiting_time - logistic_cost
    return fitness
