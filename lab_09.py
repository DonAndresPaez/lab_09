def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


def main():

    while True:
        password = input("Enter your 8-digit password: ")
        if len(password) != 8 or not password.isdigit():
            print("Invalid password format. Please enter an 8-digit password containing only integers.")
        else:
            break

    encoded_password = encode_password(password)

    print("Encoded password:", encoded_password)


if __name__ == "__main__":
    main()


tyler was here