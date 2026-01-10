import random

characters = ["A cat", "A wizard", "A robot"]
places = ["in a forest", "on Mars", "inside a castle"]
actions = ["found a treasure", "fought a dragon", "saved the world"]

story = f"{random.choice(characters)} {random.choice(places)} {random.choice(actions)}."
print("📖 Story:")
print(story)
