STEPS_GOAL = 10000

all_steps = 0

while all_steps < STEPS_GOAL:
    command = input()

    if command == "Going home":
        all_steps += int(input())
        break

    all_steps += int(command)

if all_steps >= STEPS_GOAL:
    print("Goal reached! Good job!")
    print(f"{all_steps - STEPS_GOAL} steps over the goal!")
else:
    print(f"{STEPS_GOAL - all_steps} more steps to reach goal.")