# 🔬 Simulateur de Réacteur Nucléaire

Projet en Python simulant un réacteur nucléaire fonctionnant par **fission nucléaire**. Le simulateur permet de visualiser l’évolution de la température, le comportement des neutrons et l’effet des barres de contrôle via une interface graphique simple.

## ⚙️ Fonctionnalités

- **Réacteur 2D** modélisé comme une grille (20x20).
- **Combustible nucléaire (FUEL)** : libère de l’énergie sous forme de chaleur quand un neutron provoque une fission.
- **Barres de contrôle (CONTROL_ROD)** : absorbent les neutrons pour freiner ou stopper la réaction.
- **Simulation de la température** dans chaque cellule du réacteur.
- **Production totale d’énergie** affichée dynamiquement.
- **Interface graphique (Tkinter + Matplotlib)** pour visualiser en temps réel :
  - Le cœur du réacteur (combustible, barres, neutrons).
  - La carte thermique du réacteur.
  - L’état des barres de contrôle (activables via bouton).

---

## 🖥️ Dépendances

- Python 3.7+
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (fourni avec Python)

### Installation rapide

```bash
pip install numpy matplotlib
```
### Lancement du programme

```bash
python reactor_sim.py
```
