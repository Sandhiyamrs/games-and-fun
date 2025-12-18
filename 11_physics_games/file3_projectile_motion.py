import math

print("🎯 PROJECTILE MOTION SIMULATOR\n")

velocity = float(input("Enter initial velocity (m/s): "))
angle = float(input("Enter angle of projection (degrees): "))

g = 9.8
angle_rad = math.radians(angle)

time_of_flight = (2 * velocity * math.sin(angle_rad)) / g
max_height = (velocity**2 * (math.sin(angle_rad))**2) / (2 * g)
range_distance = (velocity**2 * math.sin(2 * angle_rad)) / g

print("\n📊 RESULTS")
print("-" * 30)
print(f"Time of Flight     : {time_of_flight:.2f} seconds")
print(f"Maximum Height    : {max_height:.2f} meters")
print(f"Horizontal Range  : {range_distance:.2f} meters")
print("-" * 30)
