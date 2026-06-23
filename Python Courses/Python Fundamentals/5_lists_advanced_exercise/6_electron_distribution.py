number_of_electrons = int(input())
shell_counter = 1
filled_shells = []

while number_of_electrons > 0:
    next_shell = 2 * (shell_counter ** 2)

    if next_shell < number_of_electrons:
        filled_shells.append(next_shell)
    else:
        filled_shells.append(number_of_electrons)

    number_of_electrons -= next_shell

    shell_counter += 1

print(filled_shells)
