from src.genetic_algorithm import GeneticAlgorithm
from src.route import initialize_population
from src.utils import load_map_data

# Cargar datos del mapa
map_data = load_map_data("src/examples/map_data.json")

# Configuración del algoritmo genético
POPULATION_SIZE = 50
NUM_GENERATIONS = 100
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8

# Inicializar población
initial_population = initialize_population(POPULATION_SIZE, map_data)

# Ejecutar algoritmo genético
genetic_algo = GeneticAlgorithm(
    population=initial_population,
    map_data=map_data,
    num_generations=NUM_GENERATIONS,
    mutation_rate=MUTATION_RATE,
    crossover_rate=CROSSOVER_RATE
)

best_solution = genetic_algo.run()

# Resultados
print("Mejor ruta encontrada:", best_solution.route)
print("Fitness de la mejor ruta:", best_solution.fitness)
