import time

text = "python is fun"
print("Type:", text)
start = time.time()
typed = input()
end = time.time()

print("Time:", round(end-start, 2), "seconds")
