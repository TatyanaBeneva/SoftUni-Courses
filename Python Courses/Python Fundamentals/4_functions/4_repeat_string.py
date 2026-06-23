text = input()
counter = int(input())

repeat_string = lambda current_string, n: current_string * n
result = repeat_string(text, counter)
print(result)