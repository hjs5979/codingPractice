import math
import sys

p_list = [True] * 1000001

p_list[0] = False
p_list[1] = False

for i in range(3,int(math.sqrt(1000000))+1,2):
    if p_list[i] == False:
        continue
    
    for j in range(i*2,1000000,i):
        p_list[j] = False

while(True):
        n = int(sys.stdin.readline())

        if n==0:
            break
        
        for i in range(3,int(n/2)+1,2):
            
            if p_list[i] and p_list[n-i]:
                # print(i,n-i)
                print(str(n) +" = "+ str(i) +" + " + str(n-i))
                break

    
