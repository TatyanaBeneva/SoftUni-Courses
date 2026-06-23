number_of_lines = int(input())

is_balanced = True
has_open_bracket = False

for i in range(number_of_lines):
    current_input = input()

    if current_input == "(":
        if has_open_bracket:
            is_balanced = False
        else:
            has_open_bracket = True

    elif current_input == ")":
        if has_open_bracket:
            has_open_bracket = False
        else:
            is_balanced = False

if is_balanced and not has_open_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")