import math

# number = 100000
# count = 0

# array = [True for i in range(number+1)]

# for i in range(2, int(math.sqrt(number)+1)):
#     j = 2
#     while i * j <= number:
#         array[i*j] = False
#         j += 1

# p = []

# for i in range(2, number+1):
#     if array[i]:
#       p.append(i)
      
# if n == 2:
#     result = p[m]

# if n == 3:
#     result = p[m] ** 2
    
# if n == 4:
#     result = p[m]
# def is_prime(n):
#     for i in range(2,int(math.sqrt(n)+1)):
#             if n % i == 0:
#                 return 0
#     return 1
# def s(m):
#     count = 0
#     number = 2
        
#     while True:
        
#         if is_prime(number) == 1:
#             count += 1
            
#         number += 1
            
#         if m == count:
#             break

#     print(number-1)
    
answer = 0
number = 29000

count = 0

array = [True for i in range(number+1)]

for i in range(2, int(math.sqrt(number)+1)):
    j = 2
    while i * j <= number:
        array[i*j] = False
        j += 1
p = []

    
for i in range(2, number+1):
    if array[i]:
        p.append(i)
        
print(len(p))
