first_num = int(input())
second_num = int(input())

for n in range(first_num, second_num + 1):
    char = chr(n)
    print(f"{char}", end=" ")
