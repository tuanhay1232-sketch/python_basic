number = int(input("enter the number: "))
original_number = number


another_number = number
#new_number = 0
#count number
count = 0
while another_number > 0:
    another_number = another_number //10
    count += 1
# armstrong
total = 0
while number >0:
    digit = number %10
    total += digit ** count
    number //=10
if total == original_number:
    print(f"This number is armstrong")
else:
    print(f"This number is not armstrong")
