first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command = input().split()
    action = f"{command[0]} {command[1]}"

    if action == "Add First":
        numbers = set(map(int, command[2:]))
        first_set = first_set.union(numbers)

    elif action == "Add Second":
        numbers = set(map(int, command[2:]))
        second_set = second_set.union(numbers)

    elif action == "Remove First":
        numbers = set(map(int, command[2:]))
        first_set = first_set.difference(numbers)

    elif action == "Remove Second":
        numbers = set(map(int, command[2:]))
        second_set = second_set.difference(numbers)

    elif action == "Check Subset":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')