from collections import deque

expression = input()

stack = deque()

pairs = {
    ")": "(",
    "}": "{",
    "]": "["
}

for bracket in expression:
    if bracket in "({[":
        stack.append(bracket)

    elif not stack or stack[-1] != pairs[bracket]:
        print("NO")
        break

    else:
        stack.pop()

else:
    print("YES" if not stack else "NO")