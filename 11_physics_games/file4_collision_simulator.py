print("⚛️ ELASTIC COLLISION SIMULATOR\n")

m1 = float(input("Enter mass of object 1 (kg): "))
v1 = float(input("Enter velocity of object 1 (m/s): "))
m2 = float(input("Enter mass of object 2 (kg): "))
v2 = float(input("Enter velocity of object 2 (m/s): "))

v1_final = ((m1 - m2) / (m1 + m2)) * v1 + ((2 * m2) / (m1 + m2)) * v2
v2_final = ((2 * m1) / (m1 + m2)) * v1 + ((m2 - m1) / (m1 + m2)) * v2

print("\n📊 FINAL VELOCITIES")
print("-" * 30)
print(f"Object 1 Final Velocity : {v1_final:.2f} m/s")
print(f"Object 2 Final Velocity : {v2_final:.2f} m/s")
