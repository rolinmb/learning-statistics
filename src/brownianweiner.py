import numpy as np
import matplotlib.pyplot as plt

T = 1.0       # total time
N = 10000     # number of steps
dt = T / N    # time step
mu = 0        # drift
sigma = 1     # volatility
window_sizes = [3,11,17,23,31,47,61]  # moving average windows

if __name__ == "__main__":
    t = np.linspace(0, T, N+1)
    W = np.zeros(N+1)
    dW = np.random.normal(mu*dt, sigma*np.sqrt(dt), size=N)
    W[1:] = np.cumsum(dW)

    # Approximate derivative (Euler method)
    dW_dt = np.diff(W) / dt
    t_mid = t[:-1] + dt/2

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    # Panel 1
    ax1.plot(t, W, label="Brownian Motion", alpha=0.7)
    for window in window_sizes:
        ma = np.convolve(W, np.ones(window)/window, mode='valid')
        ax1.plot(t[window-1:], ma, label=f"MA {window} steps")
    ax1.set_ylabel("W(t)")
    ax1.set_title("Brownian Motion with Moving Averages")
    ax1.grid(True)
    ax1.legend()

    # Panel 2
    ax2.plot(t_mid, dW_dt, color='orange', label="dW/dt (Euler approx)")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("dW/dt")
    ax2.set_title("Approximate Derivative of Brownian Motion")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    plt.show()
