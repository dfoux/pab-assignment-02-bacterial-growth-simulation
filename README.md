# pab-assignment-02-bacterial-growth-simulation

## Description

This project is a Python 3 program that simulates the growth of bacterial populations on a two-dimensional rectangular grid over discrete time steps. The simulation follows an object-oriented design and was developed for the Programming Applied to Bioinformatics course.

Bacteria are represented as objects belonging to different species, with species parameters defined in an external JSON configuration file provided at runtime. The program produces both a terminal visualization of the grid and numerical population statistics logged to a CSV file.

The implementation uses only the Python standard library and prioritizes clean structure, modularity, and correctness over biological realism.

## Program Structure

The codebase is organized into modules with clear responsibilities:

- bacterium.py  
  Defines the Bacterium class representing a single bacterium. Each instance stores species properties (name, symbol, growth rate, division threshold) and maintains its internal state (size or age). It also exposes methods to update growth and to report current size/age.

- grid.py  
  Defines the Grid class representing the 2D simulation space. The grid manages cell occupancy, checks whether a cell is empty, retrieves neighboring positions (up/down/left/right), and prints the grid to the terminal using 0 for empty cells and the species symbol for occupied cells.

- simulation.py  
  Defines the Simulation class that controls the overall simulation. It initializes the grid and starting population, advances the system by one time step, runs the simulation for a given number of steps, controls how often the grid is printed, and logs population statistics to a CSV file.

- main.py  
  Entry point of the program. Parses command-line arguments, loads and validates the JSON configuration, initializes the Simulation object, and starts execution.

## Simulation Model

### Grid

- The environment is a 2D rectangular grid.
- Each cell is either empty or occupied by one bacterium.
- Multiple bacteria cannot occupy the same cell.
- Empty cells are represented by the character 0.
- Cells containing bacteria are represented by the single-character symbol defined for that species.

### Time

- The simulation runs in discrete time steps.
- At each time step, all bacteria:
  - Grow according to their growth rate.
  - Attempt division if the division threshold is reached.

### Growth and Division Rules

- At each time step, every bacterium grows according to its growth rate.
- When a bacterium reaches its division threshold:
  - It attempts to divide into a neighboring cell.
  - Division succeeds only if at least one neighboring cell is empty.
  - If division succeeds, a new bacterium of the same species is placed in the chosen empty neighboring cell.
  - If no empty neighboring cell exists, division does not occur.
- Neighboring cells are defined as up, down, left, and right.

## Inputs (Command Line)

The program must receive the following arguments via the command line:

1. Grid width
2. Grid height
3. Number of simulation steps
4. Frequency at which the grid is printed
5. Path to the JSON configuration file
6. Path to the output CSV file

## Outputs

### Grid Visualization

- The grid is printed to the terminal at the specified frequency.
- Empty cells are displayed as 0.
- Cells containing bacteria display the symbol defined for that species.

### CSV Log File

- The program generates a comma-separated CSV file.
- Each row corresponds to one simulation step (even if grid printing frequency differs).
- Each column corresponds to one bacterial species.
- The CSV file contains a header row.
- Values represent the number of bacteria of each species at each step.

## Constraints and Notes

- The program is written in Python 3.
- The program is not linear; the majority of the code resides inside functions and classes.
- All functions take at least one parameter.
- Only the Python standard library is used (no third-party packages).
- List comprehensions, dictionary comprehensions, set comprehensions, tuple comprehensions, and generator expressions are not used.
- The simulation is a computational toy model; biological realism is not required.

## License

This project is released under the MIT License. See the LICENSE file for details.
 