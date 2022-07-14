t = int(input())

n_list = list(map(int,input().split()))

max_number = max(n_list)

sieve = [True] * (max_number+1)

m = int((max_number) ** 0.5)

for i in range(2, m+1):
    if sieve[i] == True:
        for j in range(i+i, max_number+1, i):
            sieve[j] = False

p_list = [i for i in range(2, max_number+1) if sieve[i] == True]

# print(n_list, p_list,set(p_list) & set(n_list))

print(len(set(p_list) & set(n_list)))


