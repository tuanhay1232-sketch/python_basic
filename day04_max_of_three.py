"""number01 = int(input("enter the number: "))
number02 = int(input("enter the number: "))
number03 = int(input("enter the number: "))
print (max(number01, number02, number03))"""

#another way

number01 = int(input("enter the number: "))
number02 = int(input("enter the number: "))
number03 = int(input("enter the number: "))
if number01 == number02 == number03:
    print("all numbers are equal")
elif number01 >= number02 and number01 >= number03:
    print (f"{number01} is the highest number")
elif number02 >= number03 and number02 >= number01:
    print (f"{number02} is the highest number")
else:
    print (f"{number03} is the highest number")
