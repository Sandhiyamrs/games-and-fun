import random

STATES = ["Sunny", "Cloudy", "Rain", "Storm", "Fog"]

def next_state(curr):
    # simple transition probabilities biased by current state
    probs = {
        "Sunny": {"Sunny":0.7, "Cloudy":0.2, "Rain":0.05, "Storm":0.02, "Fog":0.03},
        "Cloudy": {"Sunny":0.3, "Cloudy":0.5, "Rain":0.15, "Storm":0.02, "Fog":0.03},
        "Rain": {"Cloudy":0.4, "Rain":0.45, "Storm":0.1, "Fog":0.05, "Sunny":0.0},
        "Storm": {"Rain":0.6, "Cloudy":0.2, "Storm":0.1, "Fog":0.1},
        "Fog": {"Fog":0.5, "Cloudy":0.3, "Sunny":0.2}
    }
    dist = probs.get(curr, probs["Cloudy"])
    r = random.random()
    cum = 0
    for s, p in dist.items():
        cum += p
        if r <= cum:
            return s
    return "Cloudy"

def simulate_weather(hours=24, start_temp=20):
    state = random.choice(["Sunny","Cloudy"])
    temp = start_temp
    humidity = 50
    history = []
    for h in range(hours):
        state = next_state(state)
        # temperature moves slightly by state
        if state == "Sunny":
            temp += random.uniform(0.1, 0.6)
            humidity -= random.uniform(0.5, 1.5)
        elif state == "Cloudy":
            temp += random.uniform(-0.2, 0.2)
            humidity += random.uniform(0.2, 1.0)
        elif state == "Rain":
            temp -= random.uniform(0.5, 1.5)
            humidity += random.uniform(5, 10)
        elif state == "Storm":
            temp -= random.uniform(0.5, 2.0)
            humidity += random.uniform(10, 20)
        elif state == "Fog":
            temp -= random.uniform(0.1, 0.5)
            humidity += random.uniform(5, 10)

        temp = round(temp, 1)
        humidity = max(0, min(100, round(humidity, 1)))
        history.append({"hour": h, "state": state, "temp": temp, "humidity": humidity})
    return history

if __name__ == "__main__":
    for entry in simulate_weather(24, start_temp=22):
        print(f"Hour {entry['hour']:02d}: {entry['state']:6} | {entry['temp']}°C | Humidity: {entry['humidity']}%")

