"""number = int(input("Enter the number: "))
if number <= 0:
    print("The number cannot be less than 0.")
total = 0
for i in range (1, number+1):
    total = total + i
print(f"total: {total}")"""

number = int(input("Enter the number: "))
if number <= 0:
    print("The number cannot be less than 0.")
total = 0
i = 1
while i <= number:
    total = total + i
    i += 1
print (f"total: {total}")
