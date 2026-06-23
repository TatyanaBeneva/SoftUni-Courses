def chars_between(a: str, b: str):
    char_string = ""
    for char in range(ord(a) + 1, ord(b)):
        char_string += chr(char)

    return char_string

char1 = input()
char2 = input()
string_of_chars = chars_between(char1, char2)
print(" ".join(string_of_chars))