name = input()
academy_points = float(input())
evaluators_count = int(input())

total_points = academy_points

for evaluator in range(evaluators_count):
    evaluator_name = input()
    evaluator_points = float(input())

    total_points += (len(evaluator_name) * evaluator_points) / 2

    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {name} you need {1250.5 - total_points:.1f} more!")