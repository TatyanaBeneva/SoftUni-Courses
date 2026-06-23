capacity = int(input())
fens_count = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(1, fens_count + 1):
    sector = input()

    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

print(f"{sector_a / fens_count * 100:.2f}%")
print(f"{sector_b / fens_count * 100:.2f}%")
print(f"{sector_v / fens_count * 100:.2f}%")
print(f"{sector_g / fens_count * 100:.2f}%")
print(f"{fens_count / capacity * 100:.2f}%")