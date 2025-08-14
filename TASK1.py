def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Check if character is uppercase
            if char.isupper():
                # Shift within uppercase letters (A=65 to Z=90)
                shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
                result += chr(shifted)
            else:
                # Shift within lowercase letters (a=97 to z=122)
                shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
                result += chr(shifted)
        else:
            # If not a letter, keep it unchanged
            result += char

    return result


def decrypt(text, shift):
    # Decryption is just encryption with negative shift
    return encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Encryption and Decryption ===")
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (e.g., 3): "))
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the original shift value used: "))
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
