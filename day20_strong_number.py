number = int(input("Enter the number: "))
original_number = number
total = 0
if number < 0:
    print (f"Error")
elif number ==0:
    print (f"The answer is 1")
else:
    while number >0:
        digit = number % 10
        fact = 1
        i = 1
        while i <= digit:
            fact *= i
            i += 1
        total += fact
        number //= 10
    print (f"The answer is {total}")
    if total == original_number:
        print (f"This number is a strong number")
    else:
        print (f"This number is not a strong number")
