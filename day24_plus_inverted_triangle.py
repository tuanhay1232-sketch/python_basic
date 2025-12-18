number = int(input("Enter a number: "))
i = 1
while i <= number:
    j= number
    while j >= i:
        print("*",end="")
        j-=1
    print()
    i+=1
