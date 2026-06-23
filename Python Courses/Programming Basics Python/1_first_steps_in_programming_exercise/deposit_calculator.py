deposit_sum = int(input())
deposit_deadline = int(input())
annual_interest_rate = float(input())

total_sum = deposit_sum + deposit_deadline * ((deposit_sum * (annual_interest_rate / 100)) / 12)

print(total_sum)