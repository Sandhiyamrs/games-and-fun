import random
import string

def generate():
    length = int(input("Password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    print("Generated Password:", password)

if __name__ == "__main__":
    generate()
