# models.py

import csv, random, time



class Bacterium:
    "A class to make "
    def __init__(self, species_name, symbol, growth_rate, division_threshold, size):
        self.species_name = species_name
        self.symbol = symbol
        self.growth_rate = growth_rate
        self.division_threshold = division_threshold
        self.size = size

    def grow(self):
        """
        Increase size by growth_rate.
        """
        self.size = self.size + self.growth_rate

    def get_size(self):
        return self.size


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.cells = []
        y = 0
        while y < height:
            self.cells.append([None] * width)
            y = y + 1

    def is_inside(self, x, y):
        inside = None
        if x >= 0:
            if x < self.width:
                if y >= 0:
                    if y < self.height:
                        inside = 1
        return inside

    def is_empty(self, x, y):
        empty = None
        if self.is_inside(x, y) is not None:
            if self.cells[y][x] is None:
                empty = 1
        return empty

    def place(self, x, y, bacterium):
        placed = None
        if self.is_empty(x, y) is not None:
            self.cells[y][x] = bacterium
            placed = 1
        return placed

    def get_neighbors(self, x, y):
        neighbors = []

        positions = [
            (x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
        ]

        for nx, ny in positions:
            if self.is_inside(nx, ny) is not None:
                neighbors.append((nx, ny))

        return neighbors

    def get_empty_neighbors(self, x, y):
        empty = []
        neighbors = self.get_neighbors(x, y)

        for nx, ny in neighbors:
            if self.is_empty(nx, ny) is not None:
                empty.append((nx, ny))

        return empty

    def get_all_empty_cells(self):
        empties = []
        y = 0
        while y < self.height:
            x = 0
            while x < self.width:
                if self.cells[y][x] is None:
                    empties.append((x, y))
                x = x + 1
            y = y + 1
        return empties

    def print_grid(self):
        y = 0
        while y < self.height:
            x = 0
            line_parts = []
            while x < self.width:
                cell = self.cells[y][x]
                if cell is None:
                    line_parts.append("0")
                else:
                    line_parts.append(cell.symbol)
                x = x + 1
            print(" ".join(line_parts))
            y = y + 1


class Simulation:
    def __init__(self, grid, initial_bacteria, species_names, frequency_of_grid_printing, csv_output_file):
        self.grid = grid
        self.initial_bacteria = initial_bacteria
        self.species_names = species_names
        self.frequency = frequency_of_grid_printing
        self.csv_output_file = csv_output_file

    def seed_starting_population(self):
        i = 0
        while i < len(self.initial_bacteria):
            empties = self.grid.get_all_empty_cells()
            if len(empties) == 0:
                return

            x, y = random.choice(empties)
            self.grid.place(x, y, self.initial_bacteria[i])
            i = i + 1

    def step(self):
        occupied_positions = []

        for row_index in range(self.grid.height):
            for column_index in range(self.grid.width):
                if self.grid.cells[row_index][column_index] is not None:
                    occupied_positions.append((column_index, row_index))


        for cell_x, cell_y in occupied_positions:
            bacterium_in_cell = self.grid.cells[cell_y][cell_x]

            if bacterium_in_cell is None:
                continue

            bacterium_in_cell.grow()

            if bacterium_in_cell.size >= bacterium_in_cell.division_threshold:
                empty_neighbor_cells = self.grid.get_empty_neighbors(cell_x, cell_y)

                if len(empty_neighbor_cells) > 0:
                    child_x, child_y = random.choice(empty_neighbor_cells)

                    child_bacterium = Bacterium(
                        bacterium_in_cell.species_name,
                        bacterium_in_cell.symbol,
                        bacterium_in_cell.growth_rate,
                        bacterium_in_cell.division_threshold,
                        0.0
                    )

                    self.grid.place(child_x, child_y, child_bacterium)

# Reset if needed
                    bacterium_in_cell.size = 0.0

    def count_population(self):
        counts = {}
        i = 0
        while i < len(self.species_names):
            counts[self.species_names[i]] = 0
            i = i + 1

        y = 0
        while y < self.grid.height:
            x = 0
            while x < self.grid.width:
                b = self.grid.cells[y][x]
                if b is not None:
                    counts[b.species_name] = counts[b.species_name] + 1
                x = x + 1
            y = y + 1

        return counts

    def run(self, number_of_simulation_steps):
        steps = number_of_simulation_steps

        f = open(self.csv_output_file, "w", newline="")
        try:
            w = csv.writer(f)
            w.writerow(self.species_names)

            capacity = self.grid.width * self.grid.height

            step_i = 0
            while step_i < steps:
                self.step()

                counts = self.count_population()

                row = []
                total = 0
                j = 0
                while j < len(self.species_names):
                    c = counts[self.species_names[j]]
                    row.append(c)
                    total = total + c
                    j = j + 1

                w.writerow(row)

                if self.frequency > 0:
                    if (step_i % self.frequency) == 0:
                        self.grid.print_grid()
                        print()
                        time.sleep(0.5)

                if total >= capacity:
                    break

                step_i = step_i + 1

        except:
            print("Simulation stopped by user or failed.")

        finally:
            f.close()
