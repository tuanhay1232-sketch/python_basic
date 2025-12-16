number = int(input("Enter a number: "))
original_number = number
reverse_number=0
while number >0:
    last_digit = number % 10
    reverse_number = reverse_number* 10 +last_digit
    number = number // 10
print(f"the reverse number is: {reverse_number}")
if reverse_number == original_number:
    print(f"This number is palindrome number")
else:
    print(f"This number is not palindrome number")
