import time
import numpy as np
import matplotlib.pyplot as plt


alpha = 0.8  # amplitude
p0 = alpha**2
p1 = 1 - p0
t = int(time.time())
np.random.seed(t)

if __name__ == "__main__":
    samples = np.random.choice([0,1], size=1000, p=[p0,p1])
    plt.hist(samples, bins=[-0.5,0.5,1.5], rwidth=0.6)
    plt.xticks([0,1], ['0', '1'])
    plt.ylabel("Counts")
    plt.title("Quantum Coin Measurement")
    plt.show()
