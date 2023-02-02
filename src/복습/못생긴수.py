n = int(input())

ugly = [0] * n

ugly[0] = 1

i2 = i3 = i5 = 0

ne2, ne3, ne5 = 2,3,5

for l in range(1,n):
    ugly[l] = min(ne2, ne3, ne5)
    
    if ugly[l] == ne2:
        i2 += 1
        ne2 = ugly[i2] * 2

    if ugly[l] == ne3:
        i3 += 1
        ne3 = ugly[i3] * 3
        
    if ugly[l] == ne5:
        i5 += 1
        ne5 = ugly[i5] * 5
        
print(ugly[n-1])