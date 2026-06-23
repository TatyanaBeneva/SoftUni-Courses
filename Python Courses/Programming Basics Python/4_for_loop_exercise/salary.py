tabs_count = int(input())
salary = int(input())

for n in range(tabs_count):
    site = input()

    if site == "Facebook":
        salary -= 150
    elif site == "Instagram":
        salary -= 100
    elif site == "Reddit":
        salary -= 50

    if salary <= 0:
        break

if salary > 0:
    print(salary)
else:
    print(f"You have lost your salary.")