version_list = input().split(".")
version_number = int("".join(version_list))
next_version = version_number + 1
next_version_list = [num for num in str(next_version)]

print(".".join(next_version_list))