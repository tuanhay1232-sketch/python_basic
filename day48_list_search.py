numbers = [3, 7, 2, 9, 5]
target_number = int(input("Enter your number: "))
found = False
for number in numbers:
    if target_number == number:
        found = True
        break
if found:
    print("The number is present in the list")
else:
    print("The number is not present in the list")
