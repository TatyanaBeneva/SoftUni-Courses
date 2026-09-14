expression = input()

parentheses_stack = []

for i in range(len(expression)):
    if expression[i] == '(':
        parentheses_stack.append(i)
    elif expression[i] == ')':
        start_index = parentheses_stack.pop()
        print(expression[start_index:i + 1])