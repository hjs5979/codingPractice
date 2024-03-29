a = input()
b = input()

r,c = len(a),len(b)


dp = [[0] * (c+1) for _ in range(r+1)]

for i in range(1,r+1):
    dp[i][0] = i
    
for j in range(1,c+1):
    dp[0][j] = j
    

for i in range(1, r+1):
    for j in range(1, c+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[r][c])