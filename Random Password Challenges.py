import random
import string

def generate_random_password(length):

    if length <= 0:
        raise ValueError("Password length must be a positive integer.")

    characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    random.shuffle(characters)  

    password_list = []
    for _ in range(length):
        password_list.append(random.choice(characters))

    random.shuffle(password_list)  
    return "".join(password_list)

try:
    password_length = int(input("Enter the desired password length: "))
    password = generate_random_password(password_length)
    print(f"Generated password: {password}")
except ValueError as e:
    print(f"Error: {e}")