Number = int(input("Enter a number: "))
result = 1
if Number == 0:
    print (f"The result is 1")
elif Number < 0:
    print (f"Error")
else:
    while Number > 0:
        result *= Number
        Number -= 1
    print (f"The result is {result}")


