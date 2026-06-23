string_of_numbers = input()
array_of_numbers = string_of_numbers.split(" ")
array_of_numbers = [int(number) for number in array_of_numbers]
opposite_numbers = [-number for number in array_of_numbers]

print(opposite_numbers)