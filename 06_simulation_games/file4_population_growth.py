pop = 1000
growth_rate = 0.1
for year in range(1,6):
    pop += int(pop*growth_rate)
    print(f"Year {year}: Population = {pop}")
