country = input()
device = input()

difficulty = 0
execution = 0

if country == "Russia":
    if device == "ribbon":
        difficulty = 9.100
        execution = 9.400
    elif device == "hoop":
        difficulty = 9.300
        execution = 9.800
    elif device == "rope":
        difficulty = 9.600
        execution = 9.000
elif country == "Bulgaria":
    if device == "ribbon":
        difficulty = 9.600
        execution = 9.400
    elif device == "hoop":
        difficulty = 9.550
        execution = 9.750
    elif device == "rope":
        difficulty = 9.500
        execution = 9.400
elif country == "Italy":
    if device == "ribbon":
        difficulty = 9.200
        execution = 9.500
    elif device == "hoop":
        difficulty = 9.450
        execution = 9.350
    elif device == "rope":
        difficulty = 9.700
        execution = 9.150

grade = difficulty + execution
needed_percent = ((20 - grade) / 20) * 100
print(f"The team of {country} get {grade:.3f} on {device}.\n{needed_percent:.2f}%")