numbers = [1,2,3,4,5,-6,7,8,9,10]
total=0
for number in numbers:
    if number <0:
        continue
    elif number % 2 == 0:
        total += number

print (total)
