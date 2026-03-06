# Caesar Cipher Project
# This program encrypts and decrypts text using the Caesar Cipher technique.


def caesar(text, shift, encrypt=True):
    # Validate that shift is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Shift must be between 1 and 25 (valid Caesar range)
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Define lowercase alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # If decrypting, reverse the shift
    if not encrypt:
        shift = -shift

    # Create shifted version of alphabet
    # Example: shift 3 → 'defghijklmnopqrstuvwxyzabc'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Create translation table for both lowercase & uppercase letters
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Apply translation to the text
    encrypted_text = text.translate(translation_table)
    return encrypted_text


# Function to encrypt text
def encrypt(text, shift):
    return caesar(text, shift)


# Function to decrypt text
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


# Example encrypted message
encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."

# Decrypt using shift 13 (ROT13)
decrypted_text = decrypt(encrypted_text, 13)

print(decrypted_text)
