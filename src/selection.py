import random

def tournament_selection(population, k=3):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(population, k)
        best = max(tournament, key=lambda individual: individual.fitness)
        selected.append(best)
    return selected
