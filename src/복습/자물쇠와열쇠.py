key = [[0,0,0],[1,0,0],[0,1,1]]

lock = [[1,1,1],[1,1,0],[1,0,1]]

def turn(key, n):
    
    result = [[0] * n for _ in range(n)]
    
    for r in range(n):
        for c in range(n):
            result[n-1-r][c] = key[c][r]
            
    return result

def check(new_lock, m):
    for i in range(m,m*2):
        for j in range(m,m*2):
            if new_lock[i][j] != 1:
                return False
    return True

def s(key, lock):
    n = len(key)
    m = len(lock)

    new_lock = [[0] * m*3 for _ in range(m*3)]

    for i in range(m,m*2):
        for j in range(m,m*2):
            new_lock[i][j] = lock[i-m][j-m]

    for _ in range(4):
        key = turn(key, n)
        
        for i in range(m*2):
            for j in range(m*2):
                for r in range(n):
                    for c in range(n):
                        new_lock[i+r][j+c] += key[r][c]
                
                if check(new_lock, m) == True:
                    return True
                else:
                    for r in range(n):
                        for c in range(n):
                            new_lock[i+r][j+c] -= key[r][c]
    return False
                
print(s(key,lock))              
            
    
        