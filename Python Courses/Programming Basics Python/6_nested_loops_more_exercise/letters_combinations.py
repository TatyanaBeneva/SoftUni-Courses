letter_start = input()
letter_end = input()
letter_to_not_include = input()

counter = 0

for first in range(ord(letter_start), ord(letter_end) + 1):
    for second in range(ord(letter_start), ord(letter_end) + 1):
        for third in range(ord(letter_start), ord(letter_end) + 1):

            first_letter = chr(first)
            second_letter = chr(second)
            third_letter = chr(third)

            if (
                first_letter != letter_to_not_include and
                second_letter != letter_to_not_include and
                third_letter != letter_to_not_include
            ):
                print(f"{first_letter}{second_letter}{third_letter}", end=" ")
                counter += 1

print(counter)