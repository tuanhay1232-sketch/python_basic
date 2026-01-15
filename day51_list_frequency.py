numbers = [1, 3, 5, 3, 7, 1]
for i in range(len(numbers)):
    counted= False
    for j in range(i):
        if numbers[j] == numbers[i]:
            counted = True
            break
    if counted == False:
        count = 0
        for j in range(len(numbers)):
            if numbers[j] == numbers[i]:
                count += 1
        print(f"{numbers[i]}: {count}")
