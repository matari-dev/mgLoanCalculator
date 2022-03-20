import math
number = int(input())
base = int(input())
answer = 0
if base < 2:
    answer = math.log(number)  # returns natural log of number
else:
    answer = math.log(number, base)
print(round(answer, 2))  # print answer rounded to 2 decimal places
