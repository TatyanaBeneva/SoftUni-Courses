def decrypt_word(word: str) -> str:
    character_code = ""

    for character in word:
        if character.isdigit():
            character_code += character
        else:
            break

    decoded_word = chr(int(character_code)) + word[len(character_code):]

    if len(decoded_word) <= 2:
        return decoded_word

    return (
        decoded_word[0]
        + decoded_word[-1]
        + decoded_word[2:-1]
        + decoded_word[1]
    )


encrypted_words = input().split()
decrypted_words = [decrypt_word(word) for word in encrypted_words]

print(" ".join(decrypted_words))