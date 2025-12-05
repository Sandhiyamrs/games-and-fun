import time

text = "Practice makes you perfect in typing!"

print(text)
start = time.time()
input("Type the above line: ")
end = time.time()

print(f"\nTime taken: {end - start:.2f} seconds")
