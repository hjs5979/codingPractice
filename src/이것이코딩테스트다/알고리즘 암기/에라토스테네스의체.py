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

#---------------------------------------
import numpy as np

n = int(input())

is_prime = [True for i in range(n+1)]
prime_list = []

for i in range(2,int(np.sqrt(n))+1):
    if is_prime[i]:
        j=2
        while i*j <= n:
            is_prime[i*j] = False
            j+=1

for i in range(2, n+1):
    if is_prime[i]:
        prime_list.append(i)

print(prime_list)



