
#Andres
def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

#Tyler
def decode(encoded_password):
    original_password = ""
    for char in encoded_password:
        decoded_digit = (int(char) - 3) % 10
        original_password += str(decoded_digit)
    return original_password


def main():

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
        elif option == '2':
            if 'encoded_password' in locals():
                original_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            else:
                print("No encoded password stored. Please encode a password first.")
        else:
            option == '3';
            break

if __name__ == "__main__":
    main()


