numbers = [3, 7, 2, 9, 5]
target_number = int(input("Enter your number: "))
found = False
index = -1
for i in range(len(numbers)):
    if numbers[i] == target_number:
        found = True
        index = i
        break
if found:
    print(f"the position of the number is {index}")
else:
    print(f"not found")


