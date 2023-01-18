<<<<<<< HEAD
numbers = list(map(int, list(input())))

cnt = [0,0]
temp = numbers[0]
cnt[numbers[0]] += 1

for n in range(len(numbers)):
    if temp != numbers[n]:
        cnt[numbers[n]] += 1
    temp = numbers[n]

print(min(cnt))
=======
s_number = 
>>>>>>> b8191526029f6b1e6758e732c58bf89231d47a23
