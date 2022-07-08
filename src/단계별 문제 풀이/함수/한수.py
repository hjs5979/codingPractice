n = int(input())
c = 0
if n >= 100:
    for i in range(100, n+1):
        number = list(map(int,str(i)))
        if (number[1] - number[0]) == (number[2] - number[1]):
            c+=1
    print(99 + c)

else:
    c=n
    print(c)

        