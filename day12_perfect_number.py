number = int(input("enter the number: "))
original_number = number
i=1
total=0
while i <= number // 2:
    if number % i == 0:
        total += i
    i += 1
if total == original_number:
    print(f"this number is perfect number")
else:
    print(f"this number is not perfect number")
