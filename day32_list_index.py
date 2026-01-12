numbers = [10,20,30,40,50,60,70,80,90,100]
total = 0

for i in range(len(numbers)):
    print(f"index {i} : {numbers[i]}")
    if i % 2 == 0:
        total += numbers[i]

print(total)
