from math import floor

height = float(input()) * 100
width = float(input()) * 100

available_width = width - 100

rows_by_width = floor(available_width / 70)
rows_by_height = floor(height / 120)

all_rows = (rows_by_height * rows_by_width) - 3

print(all_rows)

