import numpy as np
import matplotlib.pyplot as plt

L = 1.0
x = np.linspace(0, L, 1000)
n_values = [1, 2, 3, 5, 7, 11, 13]

if __name__ == "__main__":
    plt.figure(figsize=(10,6))
    for n in n_values:
        psi = np.sqrt(2/L) * np.sin(n * np.pi * x / L)
        P = psi**2
        plt.plot(x, P, label=f'n={n}')
    plt.xlabel("Position x")
    plt.ylabel("Probability density P(x)")
    plt.title("Quantum Particle in a 1D Box")
    plt.grid(True)
    plt.legend()
    plt.show()
