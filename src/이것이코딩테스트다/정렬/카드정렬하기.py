import heapq

n = int(input())
n_list = []
for _ in range(n):
    heapq.heappush(n_list,int(input()))

result = 0

while len(n_list) != 1:
    one = heapq.heappop(n_list)
    two = heapq.heappop(n_list)
    heapq.heappush(n_list, one+two)
    result += (one + two)

print(result)   
    
    