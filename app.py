from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from src.genetic_algorithm import GeneticAlgorithm
from src.route import initialize_population
from src.utils import load_map_data
from dotenv import load_dotenv

load_dotenv()
CORS_PERMISSIONS = os.getenv("CORS_PERMISSIONS")

app = Flask(__name__)

# Habilitar CORS
CORS(app, resources={r"/*": {"origins": CORS_PERMISSIONS}})

@app.route("/calculate_route", methods=["POST"])
def calculate_route():
    data = request.json
    map_data = data.get("map_data")
    population_size = data.get("population_size", 50)
    num_generations = data.get("num_generations", 100)
    mutation_rate = data.get("mutation_rate", 0.1)
    crossover_rate = data.get("crossover_rate", 0.8)

    if not map_data:
        return jsonify({"error": "map_data is required"}), 400

    # Inicializar población
    initial_population = initialize_population(population_size, map_data)

    # Ejecutar algoritmo genético
    genetic_algo = GeneticAlgorithm(
        population=initial_population,
        map_data=map_data,
        num_generations=num_generations,
        mutation_rate=mutation_rate,
        crossover_rate=crossover_rate
    )

    best_solution = genetic_algo.run()

    # Retornar la mejor ruta y su fitness
    return jsonify({
        "route": best_solution.route,
        "fitness": best_solution.fitness
    })

if __name__ == "__main__":
    app.run(debug=True)
