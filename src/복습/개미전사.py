n = int(input())

array = list(map(int,input().split()))

dp = [0] * n

dp[0] = array[0] 
dp[1] = array[1]

for i in range(2,n):
    if i == 2:
        dp[i] += array[i] + array[0]
    else:
        dp[i] = max(dp[i-3]+array[i],dp[i-2]+array[i])

print(max(dp))