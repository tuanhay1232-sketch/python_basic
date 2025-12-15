number = int(input("enter the number: "))
original_number = number
new_number = 0
while number > 0:
    last_digit = number%10
    new_number = new_number*10 + last_digit
    number = number//10
print (f"The reverse number is : {new_number}")
if new_number == original_number:
    print("the number is palindrome")
else:
    print("the number is not palindrome")
