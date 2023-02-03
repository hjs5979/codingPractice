n = int(input())

dp = [0] * 30001

for i in range(2,n+1):
    
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i//2] = min(dp[i//2]+1, dp[i])
    
    if i % 3 == 0:
        dp[i//3] = min(dp[i//3]+1, dp[i])
    
    if i % 5 == 0:
        dp[i//5] = min(dp[i//5]+1, dp[i])
        

print(dp[1])

    
    
