# # 소수 판별 함수

# import numpy as np

# def is_prime_number(n):
#     for i in range(2,int(np.sqrt(n))+1):
#         if n%i == 0:
#             return False
#     return True

# a = int(input())

# print(is_prime_number(a))

# #-------------------------------------------------------

# #에라토스테네스의 체

# def prime_list(n):
    
#     answer = []
#     array = [True for i in range(n+1)]
    
#     for i in range(2,int(np.sqrt(n))+1):
#         if array[i]:
#             j = 2
#             while i*j <= n:
#                 array[i*j] = False
#                 j += 1
#     for i in range(2, n+1):
#         if array[i]:
#             answer.append(i)
            
            
#     return answer

# print(prime_list(20))
         
# ---------------------------------------------------
