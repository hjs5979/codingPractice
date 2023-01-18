numbers = list(input())

numbers = list(map(int, numbers))

answer = numbers[0]
for i in range(1,len(numbers)):
    if numbers[i] == 0 or answer == 0:
        answer += numbers[i]
    else:
        answer *= numbers[i]

print(answer)


