<<<<<<< HEAD
# # 데이터 개수  N과 전체 데이터 선언
# n = int(input())
# num_list = list(map(int,input().split()))
=======
# n = int(input())
# data = list(map(int,input().split()))
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179

# # 접두사 합(Prefix Sum) 배열 계산
# sum_value = 0
# prefix_sum = [0]
<<<<<<< HEAD
# for i in num_list:
=======
# for i in data:
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
#     sum_value += i
#     prefix_sum.append(sum_value)

# # 구간 합 계산(세번째 수부터 네번째 수까지)
# left = 3
# right = 4
# print(prefix_sum[right] - prefix_sum[left-1])

<<<<<<< HEAD
#---------------------------------------
n = int(input())
num_list = list(map(int,input().split()))

sum_value = 0
prefix_sum = [0]
for i in num_list:
=======


#-----------------------------------

n = int(input())
data = list(map(int,input().split()))

sum_value = 0
prefix_sum = [0]

for i in data:
>>>>>>> 35d42c153572b0cbd616d7fa16e0d456165c8179
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4

print(prefix_sum[right] - prefix_sum[left-1])