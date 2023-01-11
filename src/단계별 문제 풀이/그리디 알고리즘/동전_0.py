n, k = map(int, input().split())

coins = []

coin_cnt = [0 for _ in range(n)]

for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

while k != 0:
    for i in range(n):
        if k >= coins[i]:
            coin_cnt[i] += (k // coins[i])
            k = (k % coins[i])
            break

print(sum(coin_cnt))


    
    



