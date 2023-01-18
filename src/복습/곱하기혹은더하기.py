<<<<<<< HEAD
s = list(map(int,input()))

answer = 0

for n in s:
    if n == 0 or n==1 or answer == 0 or answer == 1:
        answer += n
    else:
        answer *= n

print(answer)
=======
numbers = list(input())

numbers = list(map(int, numbers))

answer = numbers[0]
for i in range(1,len(numbers)):
    if numbers[i] == 0 or answer == 0:
        answer += numbers[i]
    else:
        answer *= numbers[i]

print(answer)


>>>>>>> b8191526029f6b1e6758e732c58bf89231d47a23
