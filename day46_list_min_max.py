numbers = [7, 2, 9, 4, 1, 6]
max_number = numbers[0]
min_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
    elif number < min_number:
        min_number = number
print (max_number)
print (min_number)
