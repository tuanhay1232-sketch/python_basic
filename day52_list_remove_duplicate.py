numbers = [1, 3, 5, 3, 7, 1]
result = []
for i in range(len(numbers)):
    identify = False
    for j in range(i):
        if numbers[j] == numbers[i]:
            identify = True
            break
    if identify == False:
        result.append(numbers[i])
print (result)  
