import math
import time
import random

class Enemy:
    def __init__(self, hp, speed):
        self.hp = hp
        self.speed = speed
        self.pos = 0.0  # position along path (0..path_length)
        self.alive = True

    def advance(self):
        self.pos += self.speed
        if self.pos >= 10:
            return True  # reached end
        return False

class Tower:
    def __init__(self, location, range_, damage, cooldown):
        self.location = location
        self.range = range_
        self.damage = damage
        self.cooldown = cooldown
        self.timer = 0

    def can_fire(self):
        return self.timer <= 0

    def tick(self):
        if self.timer > 0:
            self.timer -= 1

    def fire(self, enemies):
        # pick enemy closest to exit (highest pos) within range
        in_range = [e for e in enemies if e.alive and abs(e.pos - self.location) <= self.range]
        if not in_range or not self.can_fire():
            return
        target = max(in_range, key=lambda e: e.pos)
        target.hp -= self.damage
        if target.hp <= 0:
            target.alive = False
        self.timer = self.cooldown

def simulate_wave(num_enemies=5):
    enemies = [Enemy(hp=random.randint(5,10), speed=random.uniform(0.5,1.5)) for _ in range(num_enemies)]
    towers = [Tower(location=4.0, range_=3.0, damage=3, cooldown=1)]
    ticks = 0
    while any(e.alive for e in enemies):
        ticks += 1
        for tower in towers:
            tower.tick()
            tower.fire(enemies)
        for e in enemies:
            if e.alive:
                reached = e.advance()
                if reached:
                    print("An enemy reached the end!")
                    e.alive = False
        if ticks % 5 == 0:
            print(f"Tick {ticks}: alive enemies = {sum(1 for e in enemies if e.alive)}")
        time.sleep(0.05)
    print("Wave ended in", ticks, "ticks")

if __name__ == "__main__":
    simulate_wave(6)

