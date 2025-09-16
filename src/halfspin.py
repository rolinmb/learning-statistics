import time
import numpy as np
import matplotlib.pyplot as plt

N = 1000
p_up = 0.5 # 50/50 chance to observe up or down
t = int(time.time())
np.random.seed(t)
measurements = np.random.choice([1, -1], size=N, p=[p_up, 1-p_up])

if __name__ == "__main__":
    plt.hist(measurements, bins=3, edgecolor='black', align='mid')
    plt.xticks([-1, 1], ['Spin Down', 'Spin Up'])
    plt.ylabel("Counts")
    plt.title("Spin Measurement Statistics")
    plt.show()
