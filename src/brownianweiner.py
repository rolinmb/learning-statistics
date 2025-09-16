import numpy as np
import matplotlib.pyplot as plt

T = 1.0       # total time
N = 1000      # number of steps
dt = T / N    # time step
mu = 0        # drift (mean change per step)
sigma = 1     # volatility (standard deviation of step)

if __name__ == "__main__":
    # Generate Brownian motion
    t = np.linspace(0, T, N+1)                  # time array
    W = np.zeros(N+1)                           # initialize Brownian path
    dW = np.random.normal(mu * dt, sigma*np.sqrt(dt), size=N)  # random increments
    W[1:] = np.cumsum(dW)                       # cumulative sum to get the path
    plt.figure(figsize=(10, 5))
    plt.plot(t, W, label="Brownian Motion")
    plt.xlabel("Time")
    plt.ylabel("W(t)")
    plt.title("Simulation of Brownian Motion")
    plt.grid(True)
    plt.legend()
    plt.show()
