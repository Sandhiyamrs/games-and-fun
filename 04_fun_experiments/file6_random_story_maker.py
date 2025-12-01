import random

characters = ["a dragon", "an astronaut", "a robot", "a detective", "a unicorn"]
places = ["on the moon", "in a haunted house", "under the ocean", "in a secret lab"]
actions = ["found a treasure", "solved a mystery", "built a time machine", "ate 100 ice creams"]

character = random.choice(characters)
place = random.choice(places)
action = random.choice(actions)

story = f"Once upon a time, {character} went {place} and {action}!"
print("📖 Random Story Generator\n")
print(story)
