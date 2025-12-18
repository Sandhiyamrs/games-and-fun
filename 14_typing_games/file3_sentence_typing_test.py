import time

sentence = "Python is fun"
start = time.time()
input(sentence + "\n")
end = time.time()

print("Time taken:", round(end-start,2), "seconds")
