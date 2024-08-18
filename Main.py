def encrypt(text, shift):
    result = ""
    
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetical characters remain the same
            result += char
            
    return result

def decrypt(text, shift):
    # Decryption is simply the reverse process of encryption
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Would you like to encrypt or decrypt a message? (E/D): ").upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice! Please enter 'E' for encryption or 'D' for decryption.")
        return
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
