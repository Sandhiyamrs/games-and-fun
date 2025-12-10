import time, random
input("Press Enter to start...")
start = time.time()
time.sleep(random.randint(1,3))
input("Press Enter when ready!")
end = time.time()
print(f"Reaction time: {round(end-start,2)} seconds")
