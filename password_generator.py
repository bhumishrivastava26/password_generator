import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example: generate a password of length 16
user = int(input())
password = generate_password(user)
print(password)
