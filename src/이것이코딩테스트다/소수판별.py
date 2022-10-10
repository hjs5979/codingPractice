# 소수 판별 함수
import math
from tkinter import N

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2,int(math.sqrt(x))+1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0
            return False
    return True

print(is_prime_number(11))

#-------------------------------------------------------

#에라토스테네스의 체
import math

#2부터 1000까지의 모든 수에 대하여 소수판별
n = 1000

array = [True for i in range(n+1)]

# 에라토스테스의 체 알고리즘
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')



