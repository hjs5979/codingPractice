a, b = map(int,input().split())

sieve = [True] * (b+1)

m = int(b ** 0.5)

for i in range(2, m+1):
    if sieve[i] == True:
        for j in range(i+i, b+1, i):
            sieve[j] = False

p_list = [i for i in range(2, b+1) if sieve[i] == True]

answer_list = [i for i in p_list if i >= a]

for i in answer_list:
    print(i)