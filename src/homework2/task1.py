"""Homework2 - task1"""

rubles = int(input())
penny = int(input())
goods_amount = int(input())

if penny >= 100:
    rubles = rubles + penny // 100
    penny = penny % 100

total_price = str(rubles) + "." + str(penny)
total_price = float(total_price) * goods_amount
print("Total price: " + str(round(total_price, 2)))
print(total_price)
