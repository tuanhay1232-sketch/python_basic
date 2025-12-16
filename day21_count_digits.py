number = int(input("Enter a number: "))
count = 0
if number == 0:
    print("there is only one number")
else:
    while number > 0:
        number //= 10
        count += 1
    print (count)
