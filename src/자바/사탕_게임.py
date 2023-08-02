n = int(input())

array = []

for _ in range(n):
    words = list(input())
    array.append(words)

def count():
    row_count = 1
    max_row_count = 0
    col_count = 1
    max_col_count = 0
    for i in range(n):
        for j in range(n-1):
            if array[i][j] == array[i][j+1]:
                row_count += 1
            else:
                row_count = 1
            max_row_count = max(max_row_count, row_count)    
        
        # max_row_count = max(max_row_count, row_count)

    for i in range(n):
        for j in range(n-1):
            if array[j][i] == array[j+1][i]:
                col_count += 1
            else:
                col_count = 1
        # print(max_row_count)
            max_col_count = max(max_col_count, col_count)
    print(max_col_count, max_row_count)
    max_value = max(max_col_count,max_row_count)
    return max_value

answer = 0

for i in range(n):
    for j in range(n):
        
        if j < n-1:
            array[i][j], array[i][j+1] = array[i][j+1],array[i][j]
            print(array)
            left = count()
            print(left)
            array[i][j], array[i][j+1] = array[i][j+1],array[i][j]

        if i < n-1: 
            array[i][j], array[i+1][j] = array[i+1][j],array[i][j]
            down =count()
            # print(down)
            array[i][j], array[i+1][j] = array[i+1][j],array[i][j]

        answer = max(left, down)

print(answer)
            
        