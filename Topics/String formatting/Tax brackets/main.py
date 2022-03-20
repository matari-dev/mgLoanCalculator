income = int(input())
percent = 0

tier_1 = 132_407
tier_2 = 42_708
tier_3 = 15_528

if income >= tier_1:
    percent = 28
elif income >= tier_2:
    percent = 25
elif income >= tier_3:
    percent = 15

calculated_tax = round(income * percent / 100)

print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
