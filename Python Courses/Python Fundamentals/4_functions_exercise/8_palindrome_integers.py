numbers = list(map(int, input().split(", ")))

def is_palindrome(number: int):
    return str(number) == str(number)[::-1]

for number in numbers:
    print(is_palindrome(number))