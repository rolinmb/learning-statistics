import random
import time

def roll_dice(SIDES=6):
    epoch_time = time.time()
    random.seed(epoch_time)
    return random.randint(1, SIDES)

NROLLS = 10
SIDES = 6
COUNTS = {i: 0 for i in range(1, SIDES+1)}

if __name__ == "__main__":
    print(f"\nRolling a {SIDES}-sided dice {NROLLS} times")
    for i in range(NROLLS):
        result = roll_dice(SIDES)
        COUNTS[result] += 1
        print(f"src/dice.py :: Roll {i+1}: {result}")
        time.sleep(0.0001)

    print("\nOccurrences of each side:")
    for side, count in COUNTS.items():
        print(f"src/dice.py :: Side {side}: {count}")
