collumn = int(input("Enter the number of rows: "))
row = int(input("Enter the number of columns: "))
for i in range (1, collumn + 1):
    if i == 1:
        print("*" * row)
        continue
    for j in range (1, row + 1):
        if j ==1 or j == row - i +1:
            print ("*",end = "")
        else:
            print (" ",end = "")
    print ()


