import sys
import random
import numpy as np

NTRIALS = 1

def estimate_pi(trials=1):
    inside = 0
    for _ in range(trials):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    return (inside / trials) * 4

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    for i in range(1,10000):
        pi_est = estimate_pi(i)
        error = abs(np.pi - pi_est)
        print(f"src/montecarlo.py :: Estimation of π #{i}: {pi_est:.6f} -> Error: {error:.6f}")
