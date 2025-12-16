number = int(input("Enter a number: "))
reverse_number=0
while number >0:
    last_digit = number % 10
    reverse_number = reverse_number* 10 +last_digit
    number = number // 10
print(f"complete reverse number {reverse_number}")
