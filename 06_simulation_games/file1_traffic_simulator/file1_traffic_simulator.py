import random
from collections import deque
import statistics

def simulate_traffic(steps=100, arrival_prob=0.3, green_time=5, yellow_time=2, red_time=5):
    queue = deque()
    served_times = []
    light_cycle = [('G', green_time), ('Y', yellow_time), ('R', red_time)]
    cycle_index = 0
    time_in_phase = 0
    car_id = 0
    served_count = 0

    for t in range(1, steps + 1):
        # New arrivals
        if random.random() < arrival_prob:
            car_id += 1
            queue.append((car_id, t))  # (id, arrival_time)

        # Traffic light phase management
        phase, duration = light_cycle[cycle_index]
        # On green, serve up to 1 car per time unit (can be tuned)
        if phase == 'G' and queue:
            car, arrival_time = queue.popleft()
            served_times.append(t - arrival_time)
            served_count += 1

        time_in_phase += 1
        if time_in_phase >= duration:
            cycle_index = (cycle_index + 1) % len(light_cycle)
            time_in_phase = 0

        # Print status occasionally
        if t % (steps // 5 or 1) == 0:
            print(f"[t={t}] phase={phase} queue={len(queue)} served={served_count}")

    avg_wait = statistics.mean(served_times) if served_times else 0
    return {
        "total_arrived": car_id,
        "served": served_count,
        "left_in_queue": len(queue),
        "avg_wait_time": round(avg_wait, 2)
    }

if __name__ == "__main__":
    results = simulate_traffic(steps=200, arrival_prob=0.35, green_time=6, yellow_time=2, red_time=6)
    print("\nSimulation Results:", results)


