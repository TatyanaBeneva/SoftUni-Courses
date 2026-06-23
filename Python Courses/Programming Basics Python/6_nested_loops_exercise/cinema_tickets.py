standard_ticket_count = 0
kid_ticket_count = 0
student_ticket_count = 0

while True:
    movie_name = input()

    if movie_name == "Finish":
        break

    free_seats = int(input())
    movie_ticket_counter = 0

    for i in range(free_seats):
        ticket_type = input()

        if ticket_type == "End":
            break

        if ticket_type == "standard":
            standard_ticket_count += 1
        elif ticket_type == "kid":
            kid_ticket_count += 1
        elif ticket_type == "student":
            student_ticket_count += 1

        movie_ticket_counter += 1

    print(f"{movie_name} - {movie_ticket_counter / free_seats * 100:.2f}% full.")

total_tickets = standard_ticket_count + kid_ticket_count + student_ticket_count

print(f"Total tickets: {total_tickets}")
print(f"{student_ticket_count / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_ticket_count / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_ticket_count / total_tickets * 100:.2f}% kids tickets.")