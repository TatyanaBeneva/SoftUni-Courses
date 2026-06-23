from math import floor

number_of_pages_in_book = int(input())
pages_read_in_one_hour = int(input())
days_for_read = int(input())

total_hours = number_of_pages_in_book / pages_read_in_one_hour
days_hours = floor(total_hours / days_for_read)

print(days_hours)