def math_operations(*args, **kwargs):
    values = dict(kwargs)
    for index, number in enumerate(args):
        operation = index % 4

        if operation == 0:
            values["a"] += number
        elif operation == 1:
            values["s"] -= number
        elif operation == 2:
            if number != 0:
                values["d"] /= number
        else:
            values["m"] *= number
    
    sorted_values = dict(sorted(values.items(), key=lambda kvp: (-kvp[1], kvp[0])))

    return "\n".join(
        f"{key}: {value:.1f}"
        for key, value in sorted_values.items()
    )



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))

print(math_operations(6.0, a=0, s=0, d=5, m=0))
