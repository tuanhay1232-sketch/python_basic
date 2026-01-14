numbers = [2, -4, 3, 6, 0, 5, 8]
count =0
for number in numbers:
    if number % 2 == 0 and number > 0:
        count += 1
print (count)
