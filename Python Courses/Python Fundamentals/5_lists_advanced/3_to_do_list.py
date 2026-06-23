def sort_task_by_importance(tasks_list) -> list:
    sorted_list = sorted(tasks_list, key=lambda task: int(task.split("-")[0]))
    sorted_tasks_list = list(map(lambda task: task.split("-")[1], sorted_list))

    return sorted_tasks_list

all_tasks_list = []

while True:
    to_do_list = input()

    if to_do_list == "End":
        break

    all_tasks_list.append(to_do_list)

result = sort_task_by_importance(all_tasks_list)
print(result)