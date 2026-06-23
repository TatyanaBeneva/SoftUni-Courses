word = ""

has_c = False
has_o = False
has_n = False

command = input()

while command != "End":

    symbol = command

    if symbol.isalpha():

        if symbol == "c" and not has_c:
            has_c = True

        elif symbol == "o" and not has_o:
            has_o = True

        elif symbol == "n" and not has_n:
            has_n = True

        else:
            word += symbol

    if has_c and has_o and has_n:
        print(word, end=" ")

        word = ""
        has_c = False
        has_o = False
        has_n = False

    command = input()