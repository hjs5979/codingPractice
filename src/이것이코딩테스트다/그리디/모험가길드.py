n = int(input())

a_list = list(map(int,input().split()))

a_list.sort()

result = 0
count = 0

for i in a_list:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)