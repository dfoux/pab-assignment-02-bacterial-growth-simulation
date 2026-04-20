import sys
import json
from models import Bacterium, Grid, Simulation

grid_width = int(sys.argv[1])
grid_height = int(sys.argv[2])
number_of_simulation_steps = int(sys.argv[3])
frequency_of_grid_printing = int(sys.argv[4])
json_configuration_file = sys.argv[5]
csv_output_file = sys.argv[6]

with open(json_configuration_file, "r", encoding="utf-8") as json_file:
    config_data = json.load(json_file)

species_list = config_data["species"]

species_names = []
initial_bacteria = []

for species_config in species_list:
    species_name = species_config["name"]
    species_names.append(species_name)

    initial_count = species_config["initial_count"]

    for bacterium_number in range(initial_count):
        bacterium_object = Bacterium(
            species_name,
            species_config["symbol"],
            species_config["growth_rate"],
            species_config["division_threshold"],
            0.0
        )
        initial_bacteria.append(bacterium_object)


grid = Grid(grid_width, grid_height)
simulation = Simulation(grid, initial_bacteria, species_names, frequency_of_grid_printing, csv_output_file)
simulation.seed_starting_population()
simulation.run(number_of_simulation_steps)
