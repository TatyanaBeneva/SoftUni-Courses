length = int(input())
width = int(input())
heigh = int(input())
percent = float(input())

volume_of_aquarium = length * width * heigh
volume_in_litters = volume_of_aquarium * 0.001

needed_litters = volume_in_litters * (1 - (percent / 100))

print(needed_litters)