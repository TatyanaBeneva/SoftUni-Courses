words = input().split()
palindrome = input()
palindrom_list = [word for word in words if word == word[::-1]]

print(palindrom_list)
print(f"Found palindrome {palindrom_list.count(palindrome)} times")