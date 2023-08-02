n = int(input())

n_list = list(map(int,input().split()))

p_list = [True] * 1001

p_list[0] = False
p_list[1] = False

for i in range(2,1001):
    j = 2
    while i*j <= 1000:
        p_list[i*j] = False
        j+=1
answer = 0 

for i in n_list:
    if p_list[i] == True:
        answer+=1

print(answer)