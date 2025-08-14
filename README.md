Features :

🔒 Encrypt text with a shift value

🔓 Decrypt text using the original shift value

🆗 Preserves the case of letters (uppercase/lowercase)

📝 Non-alphabet characters remain unchanged

📜 User-friendly interactive menu

How It Works :

The Caesar Cipher works by shifting each letter by a set number of positions in the alphabet.
Example with a shift of 3:

Plaintext:  HELLO
Ciphertext: KHOOR

Installation  :

Clone the repository:

git clone https://github.com/your-username/caesar-cipher.git
cd caesar-cipher


Run the program:

python caesar_cipher.py

Usage

When you run the script, you’ll see a menu:

=== Caesar Cipher Encryption and Decryption ===

Options:
1. Encrypt a message
2. Decrypt a message
3. Exit


Example:

Enter your choice (1/2/3): 1
Enter the message to encrypt: Hello World!
Enter the shift value (e.g., 3): 3
Encrypted message: Khoor Zruog!

File Structure :
.
├── caesar_cipher.py   # Main Python script
└── README.md          # Documentation
