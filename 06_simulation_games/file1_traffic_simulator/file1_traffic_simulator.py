import random
import time

signals = ["Green", "Yellow", "Red"]
cars_waiting = 0

print("🚦 Traffic Simulator Started\n")

for cycle in range(5):
    signal = random.choice(signals)

    if signal == "Green":
        passed = random.randint(5, 15)
        cars_waiting = max(0, cars_waiting - passed)
        print(f"Green Light 🚦 | Cars Passed: {passed}")
    elif signal == "Yellow":
        print("Yellow Light ⚠️ | Slow Down")
    else:
        added = random.randint(3, 10)
        cars_waiting += added
        print(f"Red Light 🛑 | Cars Waiting: {cars_waiting}")

    time.sleep(1)

print("\nSimulation Ended")
