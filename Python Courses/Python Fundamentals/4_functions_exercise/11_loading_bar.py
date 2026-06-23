def loading_bar(number: int):
    step = number / 10
    loading_bar_process = ""

    for index in range(10):
        if index < step:
            loading_bar_process += "%"
        else:
            loading_bar_process += "."

    return loading_bar_process

number = int(input())
loader = loading_bar(number)

if number == 100:
    print("100% Complete!")
    print(f"[{loader}]")
else:
    print(f"{number}% [{loader}]")
    print("Still loading...")