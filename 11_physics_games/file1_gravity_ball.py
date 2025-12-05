import time
import os

def gravity_ball():
    height = 10
    gravity = 1
    bounce_factor = 0.7

    while height > 0.1:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" * int(height))
        print("   ⚽")
        height -= gravity
        time.sleep(0.1)

        if height <= 0:
            height = abs(height) * bounce_factor

gravity_ball()
