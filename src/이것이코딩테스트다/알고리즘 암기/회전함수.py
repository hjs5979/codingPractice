# def rotate_a_matrix_by_90_degree(a):
#     row_length = len(a)
#     column_length = len(a[0])
    
#     res = [[0] * row_length for _ in range(column_length)]
#     for r in range(row_length):
#         for c in range(column_length):
#             res[c][row_length -1 -r] = a[r][c]
    
#     return res

# a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# print(rotate_a_matrix_by_90_degree(a))

# ---------------------------------------------------------

n = int(input()) 

array = []

new_array = [[0]* n for _ in range(n)]

for i in range(n):
    array.append(list(map(int,input().split())))

for r in range(n):
    for c in range(n):
        new_array[r][c] = array[n-c-1][r]
        
print(new_array)
    