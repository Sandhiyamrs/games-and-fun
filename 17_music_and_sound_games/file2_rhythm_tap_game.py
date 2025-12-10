# Simulated rhythm tap (measures reaction consistency)
import time

print("Rhythm Tap Game")
input("Get ready... Press Enter to start")
print("Tap Enter 3 times to the beat!")
times = []
for i in range(3):
    input()
    times.append(time.time())
intervals = [round(times[i]-times[i-1],2) for i in range(1,len(times))]
if len(intervals) < 2:
    score = "Too few taps"
else:
    variance = max(intervals) - min(intervals)
    score = "Good" if variance < 0.3 else "OK" if variance < 0.8 else "Poor"
print("Done! Your timing score:", score)

