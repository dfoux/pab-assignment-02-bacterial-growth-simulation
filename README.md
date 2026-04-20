# Assignment 02: Bacterial Growth Simulation
### Programação Aplicada à Bioinformática (P.A.B.) Course

## 📖 Introduction
This project is a Python-based simulation designed to model the life cycle, growth, and spatial distribution of bacterial colonies on a 2D grid. Developed for the **Principles of Algorithmic Bioinformatics** (PAB) assignment, the simulation utilizes a Cellular Automata approach to visualize how different species compete for space based on biological parameters.

## ✅ Project Structure & Integrity
To satisfy the assignment requirements, the project is divided into two distinct files to separate execution logic from data modeling:

1.  **`bgc.py` (Main Execution Script):** Responsible for parsing command-line arguments using the `sys` module, loading environment settings via the `json` module, and orchestrating the simulation flow.
2.  **`models.py` (Core Logic Module):** Contains the required class definitions (`Bacterium`, `Grid`, and `Simulation`) that drive the biological and spatial logic.

The program relies exclusively on the Python standard library, ensuring it remains lightweight and portable. This architecture ensures robust state management, efficiently tracking occupied cells and processing complex biological events—such as growth cycles and mitosis within discrete, sequential time steps.

---

## 🛠️ Technical Logic Breakdown

### 1. The Biological Model (`Bacterium` class)
Defined within `models.py`, each bacterium tracks its own **size**. 
* **Growth:** Size increases by a fixed `growth_rate` per step.
* **Division:** Once size reaches the `division_threshold`, the bacterium attempts to reproduce.

### 2. Spatial Environment (`Grid` class)
This class manages a 2D coordinate system. It utilizes the `random` module for stochastic placement and a **von Neumann neighborhood** (Up, Down, Left, Right) to determine where offspring can spread.

### 3. Simulation Logic (`Simulation` class)
The simulation handles the iterative steps of the experiment, logging population dynamics using the `csv` module and optionally using `time.sleep()` to control the visual rendering speed of the grid.

---

## 📂 Configuration & Data Handling

### JSON Configuration
The simulation is highly customizable via a JSON file, allowing researchers to define multiple species with varying competitive advantages.

CODEBLOCK_1

---

## 🚀 Execution Guide

### Prerequisites
* Python 3.x
* Both `bgc.py` and `models.py` must be located in the same directory.

### Running the Simulation
```python main.py 20 20 100 100 config.json results.csv```

**Argument Breakdown:**
1. `width` / `height`: Grid dimensions.
2. `steps`: Total duration.
3. `print_freq`: Grid printing frequency (0 to disable).
4. `config.json`: Species settings.
5. `output.csv`: Destination for population results.

---

## 📊 Visual Output
When printing is enabled, the console displays a live map. `0` represents empty space, while characters represent unique species symbols.

OUTPUT_1

---

## 🔬 Scientific Analysis
* **Growth Rate vs. Threshold:** Observe how birth frequency affects dominance.
* **Spatial Exclusion:** Watch how colonies block each other's expansion.
* **Carrying Capacity:** Simulation stops automatically when the grid is saturated (total population equals grid area).

## 📄 License
Released under the MIT License.