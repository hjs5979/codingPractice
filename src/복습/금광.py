n = int(input())

for _ in range(n):

    n,m  = map(int,input().split())
    nums = list(map(int, input().split()))
    
    graph = []
    a = 0
    b = m
    for i in range(n):
        graph.append(nums[a:b])
        a += m
        b += m
        
    
    for c in range(1,m):
        for r in range(n):
            if r == 0:
                left_up = 0
            else:
                left_up = graph[r-1][c-1]
            
            if r == n-1:
                left_down = 0
            else:
                left_down = graph[r+1][c-1]
            
            left = graph[r][c-1]
            
            graph[r][c] = graph[r][c] + max(left_up, left, left_down)
    
    result = 0
    for i in range(n):
        result = max(result,graph[i][m-1])
        
    print(result)
    
    
        