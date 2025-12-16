number = int(input("Enter a number: "))
a=0
b=1
count =0
if number == 1:
    print (f"the result is 0")
elif number <=0:
    print (f"The result is error")
else:
    while count < number:
        print (a, end = " ")
        next = a+b
        a = b
        b = next
        count += 1


