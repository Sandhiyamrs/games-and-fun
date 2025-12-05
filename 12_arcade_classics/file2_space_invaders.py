import time
import os

def space_invaders():
    invaders = ["👾👾👾👾👾", "👾👾👾👾👾"]
    ship = "   🚀"

    for step in range(10):
        os.system("cls" if os.name == "nt" else "clear")
        for row in invaders:
            print(" " * step + row)
        print("\n" * 3 + ship)
        time.sleep(0.3)

space_invaders()
