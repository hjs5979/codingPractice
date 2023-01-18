import heapq

food_times = list(map(int,input().split()))
k = int(input())

if sum(food_times) <= k:
    print(-1)

q = []

for i in range(len(food_times)):
    heapq.heappush(q, (food_times[i],i+1))

sum_value = 0
previous = 0
length = len(food_times)

while sum_value + (q[0][0] * length) <= k:
    now = heapq.heappop(q)[0]
    sum_value +=  (now - previous) * length
    length -= 1
    previous = now

result = sorted(q, key=lambda x:x[1])

print(result[(k-sum_value)%length[1]]) 
    