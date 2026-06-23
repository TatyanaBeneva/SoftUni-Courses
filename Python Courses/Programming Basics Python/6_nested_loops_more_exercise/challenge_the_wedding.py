man_count = int(input())
woman_count = int(input())
tables_count = int(input())

counter = 1
is_table_finished = False

for n1 in range(1, man_count+1):
    for n2 in range(1, woman_count+1):
        print(f"({n1} <-> {n2})", end=" ")

        if tables_count == counter:
            is_table_finished = True
            break

        counter += 1

    if is_table_finished:
        break