# # 소수 판별 함수

# import numpy as np

# def is_prime_number(n):
#     for i in range(2,int(np.sqrt(n))+1):
#         if n%i == 0:
#             return False
#     return True

# a = int(input())

# print(is_prime_number(a))

#---------------------------------------

import numpy as np

n = int(input())

is_prime = True

for i in range(2, int(np.sqrt(n)+1)):
    if n%i == 0:
        is_prime = False

print(is_prime)
