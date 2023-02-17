n = int(input())

array = list(map(int,input()))

target = 1

for i in array:
    if target < i:
        break
    target += i

    
    