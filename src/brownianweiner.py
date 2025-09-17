import time
import numpy as np
import matplotlib.pyplot as plt

T = 1.0       # total time
N = 10000     # number of steps
dt = T / N    # time step
mu = 0        # drift
sigma = 1     # volatility
window_sizes = [3, 11, 17, 31, 61]  # moving average windows

epochtime = int(time.time())
np.random.seed(epochtime)

if __name__ == "__main__":
    t = np.linspace(0, T, N+1)
    W = np.zeros(N+1)
    dW = np.random.normal(mu*dt, sigma*np.sqrt(dt), size=N)
    W[1:] = np.cumsum(dW)

    # Approximate first derivative
    dW_dt = np.diff(W) / dt
    t_mid = t[:-1] + dt/2

    # Approximate second derivative
    d2W_dt2 = np.diff(dW_dt) / dt
    t_mid2 = t_mid[:-1] + dt/2

    # Approximate third derivative
    d3W_dt3 = np.diff(d2W_dt2) / dt
    t_mid3 = t_mid2[:-1] + dt/2

    fig, axs = plt.subplots(4, 1, figsize=(12, 16), sharex=True)

    # Panel 1: Brownian motion
    axs[0].plot(t, W, label="Brownian Motion", alpha=0.7)
    for window in window_sizes:
        ma = np.convolve(W, np.ones(window)/window, mode='valid')
        axs[0].plot(t[window-1:], ma, label=f"MA {window} steps")
    axs[0].set_ylabel("W(t)")
    axs[0].set_title("Brownian Motion with Moving Averages")
    axs[0].grid(True)
    axs[0].legend()

    # Panel 2: First derivative
    axs[1].plot(t_mid, dW_dt, color='orange', alpha=0.6, label="dW/dt (Euler approx)")
    for window in window_sizes:
        ma_deriv = np.convolve(dW_dt, np.ones(window)/window, mode='valid')
        t_ma = t_mid[window-1:]
        rolling_std = np.array([np.std(dW_dt[i-window+1:i+1]) for i in range(window-1, len(dW_dt))])
        axs[1].plot(t_ma, ma_deriv, label=f"Derivative MA {window} steps")
        axs[1].fill_between(t_ma, ma_deriv - rolling_std, ma_deriv + rolling_std,
            alpha=0.2, linewidth=0, label=f"±1σ (window {window})")
    axs[1].set_ylabel("dW/dt")
    axs[1].set_title("1st Derivative with MAs and Volatility Bands")
    axs[1].grid(True)
    axs[1].legend()

    # Panel 3: Second derivative
    axs[2].plot(t_mid2, d2W_dt2, color='green', alpha=0.6, label="d²W/dt²")
    for window in window_sizes:
        ma_deriv2 = np.convolve(d2W_dt2, np.ones(window)/window, mode='valid')
        t_ma2 = t_mid2[window-1:]
        rolling_std2 = np.array([np.std(d2W_dt2[i-window+1:i+1]) for i in range(window-1, len(d2W_dt2))])
        axs[2].plot(t_ma2, ma_deriv2, label=f"2nd Derivative MA {window} steps")
        axs[2].fill_between(t_ma2, ma_deriv2 - rolling_std2, ma_deriv2 + rolling_std2,
            alpha=0.2, linewidth=0, label=f"±1σ (window {window})")
    axs[2].set_ylabel("d²W/dt²")
    axs[2].set_title("2nd Derivative with MAs and Volatility Bands")
    axs[2].grid(True)
    axs[2].legend()

    # Panel 4: Third derivative
    axs[3].plot(t_mid3, d3W_dt3, color='red', alpha=0.6, label="d³W/dt³")
    for window in window_sizes:
        ma_deriv3 = np.convolve(d3W_dt3, np.ones(window)/window, mode='valid')
        t_ma3 = t_mid3[window-1:]
        rolling_std3 = np.array([np.std(d3W_dt3[i-window+1:i+1]) for i in range(window-1, len(d3W_dt3))])
        axs[3].plot(t_ma3, ma_deriv3, label=f"3rd Derivative MA {window} steps")
        axs[3].fill_between(t_ma3, ma_deriv3 - rolling_std3, ma_deriv3 + rolling_std3,
            alpha=0.2, linewidth=0, label=f"±1σ (window {window})")
    axs[3].set_xlabel("Time")
    axs[3].set_ylabel("d³W/dt³")
    axs[3].set_title("3rd Derivative with MAs and Volatility Bands")
    axs[3].grid(True)
    axs[3].legend()

    plt.tight_layout()
    plt.show()
