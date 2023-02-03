n,k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)
i = 0
for j in range(len(a)):
    if b[i] > a[j]:
        a[j] = b[i]
        i+=1
        if i == k:
            break
    else:
        break

print(sum(a))