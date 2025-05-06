import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random

# Constantes
GRID_SIZE = 20
EMPTY = 0
FUEL = 1
CONTROL_ROD = 3
FISSION_ENERGY = 200  # MeV
ENERGY_TO_TEMP_FACTOR = 0.05
TEMP_COOLING_RATE = 0.98
CONTROL_ROD_ABSORPTION_PROB = 0.9

# Initialisation
core = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
core[8:12, 8:12] = FUEL
core[8:12, 9:11] = CONTROL_ROD

# État des neutrons
neutrons = np.zeros_like(core, dtype=bool)
neutrons[10, 8] = True 
temperature = np.zeros_like(core, dtype=float)
total_energy_output = 0
control_rod_state = 1

def simulate_step():
    global neutrons, temperature, total_energy_output, control_rod_state
    new_neutrons = np.zeros_like(neutrons)
    
    print("Neutron map:\n", neutrons.astype(int))

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if neutrons[i, j]:
                if core[i, j] == FUEL:
                    # Échappement d'énergie
                    total_energy_output += FISSION_ENERGY
                    temperature[i, j] += FISSION_ENERGY * ENERGY_TO_TEMP_FACTOR
                    print(f"Fission at ({i}, {j}), Energy: {FISSION_ENERGY}")

                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < GRID_SIZE and 0 <= nj < GRID_SIZE:
                                new_neutrons[ni, nj] = True
                elif core[i, j] == CONTROL_ROD:
                    if control_rod_state == 1:
                        if random.random() > CONTROL_ROD_ABSORPTION_PROB:
                            new_neutrons[i, j] = True
                    else:
                        new_neutrons[i, j] = True
                else:
                    new_neutrons[i, j] = True

    # Dissipation de la chaleur
    temperature *= TEMP_COOLING_RATE
    neutrons = new_neutrons

class ReactorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Reactor Simulation")
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack()

        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack()

        self.control_btn = ttk.Button(root, text="Toggle Control Rods", command=self.toggle_control_rods)
        self.control_btn.pack(pady=10)

        self.energy_label = ttk.Label(root, text="Total Energy Output: 0 MeV")
        self.energy_label.pack()

        self.update()

    def toggle_control_rods(self):
        global control_rod_state
        control_rod_state = 1 - control_rod_state
        print(f"Control rods state: {'Inserted' if control_rod_state else 'Withdrawn'}")

    def update(self):
        if not self.root.winfo_exists():
            return
        
        simulate_step()

        # Affichage des neutrons et de la température
        display_neutrons = np.zeros_like(core)
        display_neutrons[neutrons] = 1

        self.ax1.clear()
        self.ax1.set_title("Reactor Core")
        self.ax1.imshow(display_neutrons, cmap='Blues', interpolation='nearest')

        self.ax2.clear()
        self.ax2.set_title("Temperature")
        self.ax2.imshow(temperature, cmap='inferno', interpolation='nearest')

        # Calculer l'énergie totale
        print(f"Total Energy: {total_energy_output} MeV")
        self.energy_label.config(text=f"Total Energy Output: {int(total_energy_output)} MeV")

        self.canvas.draw()

        # Mettre à jour l'affichage toutes les 200 ms
        self.root.after(200, self.update)

root = tk.Tk()
app = ReactorGUI(root)
root.mainloop()