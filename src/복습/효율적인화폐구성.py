n, m = map(int,input().split())

array =[]

for _ in range(n):
    array.append(int(input()))

dp = [1e9] * (m+1)

# for i in array:
    # dp[i] = i

dp[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if dp[j-array[i]] != 1e9:
            dp[j] = min(dp[j], dp[j-array[i]]+1)

print(dp[m] if dp[m] != 1e9 else -1)