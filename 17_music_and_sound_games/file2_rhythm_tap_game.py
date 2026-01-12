import time

print("Tap ENTER when ready!")
time.sleep(2)
start = time.time()
input()
end = time.time()

print("Reaction time:", round(end - start, 2), "seconds")
