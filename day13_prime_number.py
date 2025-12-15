number = int(input("enter the number: "))
original_number = number
i=2
is_prime = True
if number <=1:
    print (f"{number} is not a prime number")
else:
    while i <= number//2:
        if number % i ==0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

