import math

a, b, c = map(int, input().split())

if b >= c :
    n = -1
    print(n)
else:
    n =  math.floor(-a/(b-c))
    while True:
        n += 1
        if (a + n*(b-c)) < 0:
            break
    print(n)
