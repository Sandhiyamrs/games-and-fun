import math
import time
import os

def spring_motion():
    for t in range(200):
        os.system("cls" if os.name == "nt" else "clear")
        x = int(10 * math.sin(t * 0.2))
        print(" " * (x + 20) + "🔵")
        time.sleep(0.05)

spring_motion()
