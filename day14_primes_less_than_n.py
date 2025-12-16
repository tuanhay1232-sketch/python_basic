number = int(input("enter the number: "))
current = 2
while current <= number:
    i = 2
    is_prime = True
    while i<= current //2:
        if current % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(current, end = " ")
    current += 1
