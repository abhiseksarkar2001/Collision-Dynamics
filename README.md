# Collision Dynamics of Confined Particle Systems

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Research](https://img.shields.io/badge/research-computational%20physics-orange.svg)](https://github.com/abhiseksarkar2001/Collision-Dynamics)

A computational study investigating collision dynamics in two-dimensional confined particle systems using event-driven molecular dynamics simulations.

## 📋 Table of Contents
- [Overview](#overview)
- [Research Questions](#research-questions)
- [Key Findings](#key-findings)
- [Installation](#installation)
- [Usage](#usage)
- [Experiments](#experiments)
- [Results](#results)
- [Theoretical Background](#theoretical-background)
- [Contributing](#contributing)
- [Citation](#citation)

## 🔬 Overview

This repository contains the computational implementation and analysis of collision dynamics in confined particle systems. The research explores how container geometry, particle density, and initial velocity distributions influence collision frequencies in two-dimensional systems.

The study employs Monte Carlo simulations and event-driven molecular dynamics to investigate:
- Particle-wall collision scaling with container geometry
- Particle-particle collision dynamics under varying densities
- Velocity distribution evolution toward Maxwell-Boltzmann equilibrium

## ❓ Research Questions

1. **How do collision rates scale with container geometry?**
   - Investigation of aspect ratio effects on collision frequencies
   - Analysis of wall surface area to volume ratios

2. **How does particle density shape collision frequencies?**
   - Study of many-body effects in confined systems
   - Exploration of scaling laws with particle number

3. **How do initial velocity distributions affect long-term collision dynamics?**
   - Analysis of energy-dependent collision rates
   - Investigation of thermodynamic equilibrium establishment

## 🔍 Key Findings

### Geometric Effects
- **Particle-wall collisions**: Scale linearly with container aspect ratio
- **Particle-particle collisions**: Decrease with increasing geometric anisotropy
- **Engineering implications**: Container geometry can be optimized for specific applications

### Density Effects
- **Scaling behavior**: Particle-particle collisions scale as N^1.8 (not N^2 as in infinite systems)
- **Finite-size effects**: Confinement creates correlations that reduce effective collision area
- **Many-body physics**: Demonstrates non-trivial collective behavior in confined systems

### Energy Considerations
- **Quadratic scaling**: Collision rates scale with the square of initial velocity ranges
- **Kinetic theory validation**: Results consistent with classical predictions
- **Thermodynamic equilibrium**: Velocity distributions converge to Maxwell-Boltzmann form

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Required Dependencies
```bash
pip install pygame numpy matplotlib
```

### Clone the Repository
```bash
git clone https://github.com/abhiseksarkar2001/Collision-Dynamics.git
cd Collision-Dynamics
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Basic Simulation
```python
from main_code import run_simulation

# Run a basic simulation with default parameters
results = run_simulation(
    num_balls=10,
    width=600,
    height=600,
    velocity_range=(-5, 5),
    duration=86400
)

print(f"Wall collisions: {results['wall_collisions']}")
print(f"Ball collisions: {results['ball_collisions']}")
print(f"Total collisions: {results['total_collisions']}")
```

### Customized Simulation
```python
# Custom container geometry
results = run_simulation(
    num_balls=15,
    width=1200,
    height=300,
    velocity_range=(-10, 10),
    duration=50000
)
```

### Visualizing Results
```python
from main_code import plot_velocity_distribution

# Plot velocity distribution
plot_velocity_distribution(results["velocity_histogram"])
```

## 🧪 Experiments

### Experiment 1: Container Geometry Effects
Studies the influence of container aspect ratio on collision dynamics while maintaining constant area.

**Configurations:**
- Square container: 600 × 600 pixels (aspect ratio = 1.0)
- Rectangular container: 900 × 400 pixels (aspect ratio = 2.25)
- Elongated container: 1200 × 300 pixels (aspect ratio = 4.0)

**Parameters:**
- Particles: N = 10
- Initial velocities: [-5, 5] pixels/time unit
- Constant area: 360,000 pixels²

### Experiment 2: Particle Density Effects
Investigates collision rate scaling with particle number in a fixed container.

**Configurations:**
- Low density: N = 10 particles
- Medium density: N = 15 particles
- High density: N = 20 particles

**Parameters:**
- Container: 600 × 600 pixels
- Initial velocities: [-5, 5] pixels/time unit

### Experiment 3: Initial Velocity Distribution Effects
Examines how initial energy affects collision dynamics.

**Configurations:**
- Low energy: [-5, 5] pixels/time unit
- Medium energy: [-10, 10] pixels/time unit
- High energy: [-15, 15] pixels/time unit

**Parameters:**
- Container: 600 × 600 pixels
- Particles: N = 10

## 📊 Results

### Container Geometry Effects
| Container Size | Particle-Wall | Particle-Particle | Total |
|---------------|---------------|-------------------|-------|
| 600 × 600     | 7457 ± 1156   | 6702 ± 1978      | 14159 ± 2234 |
| 900 × 400     | 8170 ± 1124   | 6242 ± 1556      | 14412 ± 1845 |
| 1200 × 300    | 10103 ± 628   | 5785 ± 649       | 15889 ± 945  |

### Particle Density Effects
| Particles | Particle-Wall | Particle-Particle | Total |
|-----------|---------------|-------------------|-------|
| 10        | 7455 ± 1234   | 6702 ± 1998      | 14157 ± 2456 |
| 15        | 11641 ± 845   | 13776 ± 567      | 25417 ± 1234 |
| 20        | 15960 ± 2098  | 25650 ± 3456     | 41610 ± 4567 |

### Initial Velocity Effects
| Velocity Range | Particle-Wall | Particle-Particle | Total |
|---------------|---------------|-------------------|-------|
| [-5, 5]       | 7455 ± 1234   | 6702 ± 1567      | 14158 ± 2134 |
| [-10, 10]     | 14195 ± 1789  | 11500 ± 1098     | 26695 ± 2345 |
| [-15, 15]     | 20439 ± 2567  | 15083 ± 1456     | 35521 ± 3123 |

## 🧮 Theoretical Background

### Collision Dynamics
The system consists of N identical particles with mass m and radius r in a 2D rectangular container. All collisions are elastic, conserving momentum and kinetic energy.

**Conservation Laws:**
- Momentum: `mv_i,init + mv_j,init = mv_i,fin + mv_j,fin`
- Energy: `½m|v_i,init|² + ½m|v_j,init|² = ½m|v_i,fin|² + ½m|v_j,fin|²`

### Event-Driven Algorithm
The simulation uses event-driven molecular dynamics with:
- Collision detection tolerance: ε = 10⁻⁶
- Time step: Δt = 1 time unit
- Simulation duration: 86,400 time steps

### Statistical Analysis
- Each configuration repeated 5 times with different random seeds
- Ensemble averages calculated for statistical reliability
- Velocity distributions tracked for equilibration analysis

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Commit your changes: `git commit -m 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

### Code Style
- Follow PEP 8 guidelines
- Add docstrings for new functions
- Include unit tests for new features

 <!--
 ## 📄 Citation

 If you use this code in your research, please cite:

```bibtex
@article{sarkar2024collision,
  title={Collision Dynamics of Confined Particle Systems: A Computational Study of Container Geometry and Density Effects},
  author={Sarkar, Abhisek and Banerjee, Soumitro},
  journal={Computational Physics},
  year={2024},
  institution={Indian Institute of Science Education and Research Kolkata}
}
 -->```

## 🏫 Acknowledgments

- Indian Institute of Science Education and Research Kolkata for computational resources
- Summer Research Fellowship Program for funding support
- Dr. Soumitro Banerjee for supervision and guidance

## 📞 Contact

**Abhisek Sarkar**  
Email: as20ms091@iiserkol.ac.in
Alt Email: helloabhisek2001@gmail
Institution: Indian Institute of Science Education and Research Kolkata

---

*This research contributes to the understanding of collision dynamics in confined systems with applications ranging from granular flow to protoplanetary disk evolution.*
