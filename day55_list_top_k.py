numbers = [5, 2, 9, 1, 3]
K = int(input("Enter the number: "))
for i in range(K):
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
print(numbers[:K])
