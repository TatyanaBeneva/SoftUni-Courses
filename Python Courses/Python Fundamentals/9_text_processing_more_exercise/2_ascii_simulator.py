start_ord = ord(input())
end_ord = ord(input())
text = input()
total_sum = 0

for char in text:
    if start_ord < ord(char) < end_ord:
        total_sum += ord(char)

print(total_sum)