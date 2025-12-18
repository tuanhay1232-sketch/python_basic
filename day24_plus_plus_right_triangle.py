number = int(input("Enter a number: "))
i = 1
while i <= number:
    space = number - i
    spaces = space * " "
    print(spaces,end= "")
    j= 1
    while j <= i:
        print("*",end="")
        j +=1
    print()
    i+=1
