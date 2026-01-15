numbers = [1, 3, 5, 3, 7]
has_duplicates = False
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] == numbers[j]:
            has_duplicates = True
            break
print (has_duplicates)
