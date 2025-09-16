import random
import time

NROLLS = 100
SIDES = 20
COUNTS = {i: 0 for i in range(1, SIDES+1)}

def roll_dice(s=6):
    epoch_time = int(time.time() * 1000)
    random.seed(epoch_time)
    return random.randint(1, s)

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
