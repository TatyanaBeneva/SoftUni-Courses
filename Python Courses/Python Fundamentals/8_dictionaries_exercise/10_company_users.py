companies = {}

while True:
    data = input()

    if data == "End":
        break

    company, employee_id = data.split(" -> ")

    if company not in companies:
        companies[company] = [employee_id]
    else:
        if employee_id not in companies[company]:
            companies[company].append(employee_id)

for key, value in companies.items():
    print(f'{key}')
    for employee_id in value:
        print(f'-- {employee_id}')