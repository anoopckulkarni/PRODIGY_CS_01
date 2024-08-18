# Caesar Cipher Encryption/Decryption

Done by Anoop C Kulkarni


This Python program allows users to encrypt and decrypt messages using the Caesar Cipher algorithm. The Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is shifted by a certain number of positions down or up the alphabet.

## Features

- **Encryption**: Converts plain text into cipher text by shifting each character by a user-defined value.
- **Decryption**: Converts cipher text back into plain text by reversing the shift.
- Handles both uppercase and lowercase characters.
- Non-alphabetical characters (e.g., numbers, spaces, punctuation) are unaffected by the cipher.

## Requirements

- Python 3.x

## Usage

1. **Clone the Repository** (if hosted on a version control system like GitHub) or download the `caesar_cipher.py` file directly.

2. **Run the Program**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `caesar_cipher.py`.
   - Run the program using the command:
     ```bash
     python caesar_cipher.py
     ```

3. **Follow the Prompts**:
   - **Choose Operation**: Enter `E` to encrypt a message or `D` to decrypt a message.
   - **Enter the Message**: Type the message you want to encrypt or decrypt.
   - **Enter the Shift Value**: Provide an integer value for the shift (positive for right shift, negative for left shift).

4. **View the Output**:
   - The program will display the encrypted or decrypted message based on your inputs.

## Example

```bash
Caesar Cipher Encryption/Decryption
Would you like to encrypt or decrypt a message? (E/D): E
Enter the message: Hello World!
Enter the shift value (integer): 3
Encrypted message: Khoor Zruog!
```

```bash
Caesar Cipher Encryption/Decryption
Would you like to encrypt or decrypt a message? (E/D): D
Enter the message: Khoor Zruog!
Enter the shift value (integer): 3
Decrypted message: Hello World!
```

## Notes

- The Caesar Cipher algorithm only shifts letters in the alphabet. Non-alphabetical characters (like numbers, spaces, and punctuation) will remain unchanged.
- The shift value should be an integer. If you want to reverse the encryption, use the negative of the shift value used during encryption.


## Contributing

Feel free to fork this project, submit issues, or contribute by creating pull requests.
