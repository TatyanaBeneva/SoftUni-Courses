from collections import deque

stack = deque()

lines = int(input())

for _ in range(lines):
    command = input().split()
    action = int(command[0])

    if action == 1:
        number = int(command[1])
        stack.append(number)

    elif action == 2 and stack:
        stack.pop()

    elif action == 3 and stack:
        print(max(stack))

    elif action == 4 and stack:
        print(min(stack))

print(", ".join(str(x) for x in reversed(stack)))