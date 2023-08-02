import math

a,b = map(int,input().split())

p_list = [True] * (b+1)

p_list[0] = False
p_list[1] = False

for i in range(2,int(math.sqrt(b))+1):
    if p_list[i] == False:
        continue;
    
    for j in range(2*i,b+1,i):
        p_list[j] = False

for i in range(a,b+1):
    if p_list[i] == True:
        print(i)