pens = int(input())
markers = int(input())
liters_of_detergent = int(input())
discount = int(input())

pen_price = 5.80
marker_price = 7.20
detergent_price = 1.20

total_sum = pens * pen_price + markers * marker_price + liters_of_detergent * detergent_price
total_sum_with_discount = total_sum - (total_sum * (discount / 100))

print(total_sum_with_discount)
