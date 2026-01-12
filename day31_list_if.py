number= [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in number:
    if i % 2 == 0:
        print(i)
    if i > 5:
        sum = sum + i
print (sum)
