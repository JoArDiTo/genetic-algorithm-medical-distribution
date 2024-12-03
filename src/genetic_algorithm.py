import random
from src.fitness import calculate_fitness
from src.route import crossover, mutate
from src.selection import tournament_selection

class GeneticAlgorithm:
    def __init__(self, population, map_data, num_generations, mutation_rate, crossover_rate):
        self.population = population
        self.map_data = map_data
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate

    def run(self):
        for generation in range(self.num_generations):
            # Calcular fitness
            for individual in self.population:
                individual.fitness = calculate_fitness(individual, self.map_data)

            # Selección
            selected_parents = tournament_selection(self.population)

            # Cruzamiento y mutación
            next_population = []
            for i in range(0, len(selected_parents), 2):
                parent1, parent2 = selected_parents[i], selected_parents[i+1]
                if random.random() < self.crossover_rate:
                    child1, child2 = crossover(parent1, parent2)
                else:
                    child1, child2 = parent1, parent2

                if random.random() < self.mutation_rate:
                    mutate(child1)
                if random.random() < self.mutation_rate:
                    mutate(child2)

                next_population.extend([child1, child2])

            self.population = next_population

        return max(self.population, key=lambda individual: individual.fitness)
