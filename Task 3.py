import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z'
]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['@','#','&','%','!']
def get_user_input():
    # Prompt the user to enter the desired length of the password
    print("PASSWORD GENERATOR")
    length = int(input("Enter the  length of the password: "))
    return length
def generate_password(length):
    # Combine letters and numbers into one list
    all_characters = letters + numbers + symbols
    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
def display_password(password):
    # Print the generated password on the screen
    print(f"Generated Password: {password}")
def main():
    length = get_user_input()
    password = generate_password(length)
    display_password(password)

if __name__ == "__main__":
    main()
