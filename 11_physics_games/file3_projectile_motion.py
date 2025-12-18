import math

v = float(input("Enter velocity: "))
angle = float(input("Enter angle (degrees): "))

g = 9.8
angle_rad = math.radians(angle)
time = (2 * v * math.sin(angle_rad)) / g
range_ = (v**2 * math.sin(2 * angle_rad)) / g

print("Time of flight:", round(time, 2))
print("Range:", round(range_, 2))
