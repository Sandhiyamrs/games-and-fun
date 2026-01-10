population = 1000
growth_rate = 0.05

print("👥 Population Growth Simulation\n")

for year in range(1, 11):
    population += int(population * growth_rate)
    print(f"Year {year}: Population = {population}")
