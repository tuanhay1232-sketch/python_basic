number = int(input("enter the number: "))
original_number = number
new_number = 0
while number > 0:
    last_digit = number%10
    new_number += last_digit
    number = number//10
print(new_number)
