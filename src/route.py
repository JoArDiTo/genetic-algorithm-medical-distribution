import random

class Route:
    def __init__(self, route):
        self.route = route  # Lista de puntos de la ruta
        self.fitness = 0

def initialize_population(size, map_data):
    points = list(map_data.keys())
    population = [Route(random.sample(points, len(points))) for _ in range(size)]
    return population

def crossover(parent1, parent2):
    # Cruzamiento por orden (OX)
    size = len(parent1.route)
    start, end = sorted(random.sample(range(size), 2))
    child1_route = parent1.route[start:end]
    child2_route = parent2.route[start:end]

    child1_route += [point for point in parent2.route if point not in child1_route]
    child2_route += [point for point in parent1.route if point not in child2_route]

    return Route(child1_route), Route(child2_route)

def mutate(route):
    # Mutación por intercambio
    idx1, idx2 = random.sample(range(len(route.route)), 2)
    route.route[idx1], route.route[idx2] = route.route[idx2], route.route[idx1]
