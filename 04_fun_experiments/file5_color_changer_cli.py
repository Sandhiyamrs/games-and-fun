import time
import itertools

colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]

print("🎨 Color Changing Text")

for color in itertools.cycle(colors):
    print(color + "Python is Fun!" + "\033[0m", end="\r")
    time.sleep(0.4)
