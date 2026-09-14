from collections import deque
from datetime import datetime, timedelta

robots_data = input().split(";")
start_time = datetime.strptime(input(), "%H:%M:%S")

robots = []

for robot_data in robots_data:
    name, process_time = robot_data.split("-")

    robots.append({
        "name": name,
        "process_time": int(process_time),
        "busy_until": 0
    })

products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

current_second = 0

while products:
    current_second += 1
    product = products.popleft()

    free_robot = None

    for robot in robots:
        if robot["busy_until"] <= current_second:
            free_robot = robot
            break

    if free_robot:
        current_time = start_time + timedelta(seconds=current_second)

        print(
            f"{free_robot['name']} - {product} "
            f"[{current_time.strftime('%H:%M:%S')}]"
        )

        free_robot["busy_until"] = (
            current_second + free_robot["process_time"]
        )

    else:
        products.append(product)