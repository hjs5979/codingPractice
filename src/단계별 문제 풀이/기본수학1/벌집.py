target = int(input())

n = 1
if target == 1:
        print(1)
else:
    while True:

        if target in range(3*(n)**2-3*(n)+2,3*(n+1)**2-3*(n+1)+2):
            break
        
        else:
            n+=1

    print(1+n)