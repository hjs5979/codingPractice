min_number = int(input())
max_number = int(input())

sieve = [True] * (max_number+1)

m = int((max_number) ** 0.5)

for i in range(2, m+1):
    if sieve[i] == True:
        for j in range(i+i, max_number+1, i):
            sieve[j] = False

p_list = [i for i in range(2, max_number+1) if sieve[i] == True]

answer_list = [i for i in p_list if i >= min_number]


if len(answer_list) == 0:
    print(-1)

else:
    print(sum(answer_list))
    print(min(answer_list))
