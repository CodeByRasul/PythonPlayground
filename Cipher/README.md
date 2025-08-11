# Vigenère Cipher

A Python implementation of the classic Vigenère cipher for encrypting and decrypting text messages.

## About

The Vigenère cipher is a method of encrypting alphabetic text using a simple form of polyalphabetic substitution. It uses a repeating keyword to shift letters in the alphabet, making it more secure than simple Caesar ciphers.

## Features

- ✅ Encrypt text messages using a custom key
- ✅ Decrypt encrypted messages with the same key
- ✅ Handles both uppercase and lowercase letters
- ✅ Preserves non-alphabetic characters (spaces, punctuation, numbers)
- ✅ Clean and readable code structure

## How It Works

The Vigenère cipher works by:
1. Taking a plaintext message and a keyword
2. Repeating the keyword to match the length of the message
3. Shifting each letter in the message by the corresponding letter value in the key
4. For decryption, the process is reversed by shifting in the opposite direction

### Example
```
Message: "hello world"
Key:     "happycoding"
Result:  "oiwwc kvhwr"
```

## Usage

### Basic Example
```python
# Sample encrypted text and key
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

# Decrypt the message
decryption = decrypt(text, custom_key)
print(f'Decrypted text: {decryption}')
```

### Encrypt Your Own Message
```python
# Encrypt a message
message = "your secret message"
key = "yourkey"
encrypted = encrypt(message, key)
print(f'Encrypted: {encrypted}')

# Decrypt it back
decrypted = decrypt(encrypted, key)
print(f'Decrypted: {decrypted}')
```

## Functions

### `vigenere(message, key, direction=1)`
Core function that handles both encryption and decryption.
- `message`: Text to encrypt/decrypt
- `key`: Keyword for the cipher
- `direction`: 1 for encryption, -1 for decryption

### `encrypt(message, key)`
Encrypts a message using the provided key.

### `decrypt(message, key)`
Decrypts a message using the provided key.

## Requirements

- Python 3.x
- No external libraries required

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/vigenere-cipher.git
```

2. Navigate to the project directory:
```bash
cd vigenere-cipher
```

3. Run the script:
```bash
python vigenere_cipher.py
```

## Example Output

```
Encrypted text: mrttaqrhknsw ih puggrur
Key: happycoding

Decrypted text: vigenere is awesome
```

## Security Note

While the Vigenère cipher was considered unbreakable for centuries (earning it the nickname "le chiffre indéchiffrable"), it can be broken using modern cryptanalysis techniques. This implementation is for educational purposes and should not be used for securing sensitive information.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

---

⭐ **Star this repository if you found it helpful!** ⭐
