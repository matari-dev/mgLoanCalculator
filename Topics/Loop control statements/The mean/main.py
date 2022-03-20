numbers = []
number = input()
while number != '.':
    numbers.append(int(number))
    number = input()
print(sum(numbers) / len(numbers))
