from collections import Counter

n = int(input())
stages = list(map(int,input().split()))

a = Counter(stages)

answer = []

l = len(stages)
for i in range(1,n+1):
     
    answer.append((i,a[i]/l))
    l -= a[i]
    
answer.sort(key=lambda x:-x[1])

answer = [i[0] for i in answer]
print(answer)

#count = stages.count(i)