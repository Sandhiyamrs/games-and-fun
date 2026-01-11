import math

v = 20
g = 9.8

for t in range(5):
    y = v*t - 0.5*g*t*t
    print(f"Time {t}s -> Height {y:.2f}")
