m = int(input())

count = 0
password = ""

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):

                if a < b and c > d:
                    result = a * b + c * d

                    if result == m:
                        print(f"{a}{b}{c}{d}", end=" ")
                        count += 1

                        if count == 4:
                            password = f"{a}{b}{c}{d}"

print()

if password:
    print(f"Password: {password}")
else:
    print("No!")