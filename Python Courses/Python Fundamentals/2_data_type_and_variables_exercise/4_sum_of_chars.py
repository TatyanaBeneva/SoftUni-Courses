n = int(input())
char_sum = 0

for i in range(n):
    char = input()
    char_num = ord(char)
    char_sum += char_num

print(f"The sum equals: {char_sum}")