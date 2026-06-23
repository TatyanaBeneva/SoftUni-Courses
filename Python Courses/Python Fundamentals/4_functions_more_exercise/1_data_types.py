def string_action(type: str, string: str):
    result = ""
    if type == "int":
        result = int(string) * 2
    elif type == "real":
        result = float(string) * 1.5
        result = f"{result:.2f}"
    elif type == "string":
        result = f"${string}$"

    return result

type = input()
string = input()

print(string_action(type, string))