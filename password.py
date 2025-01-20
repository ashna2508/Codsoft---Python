import random

# Lists of numbers, lowercase letters, and uppercase letters
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "y", "u", "v", "w", "x", "y", "z"]
u_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "Y", "U", "V", "W", "X", "Y", "Z"]

def generate_password(length):
    password = ""
    for _ in range(length):
        # Randomly choose from numbers, lowercase, or uppercase letters
        char_type = random.choice([numbers, l_alpha, u_alpha])
        password += str(random.choice(char_type))
    return password

# Generate a 12-character password
password_length = 12
print("Generated Password:", generate_password(password_length))