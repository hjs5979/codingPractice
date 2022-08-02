s = list(map(int,input()))

answer = 0

for n in s:
    if n == 0 or n==1 or answer == 0 or answer == 1:
        answer += n
    else:
        answer *= n

print(answer)