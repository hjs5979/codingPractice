

target = int(input())
n =  1

while True:
    
    if target in range(int(1+((n-1)*n)/2),int(1+((n)*(n+1)/2))):
        break
    else:
        n+=1

c = target - int(1+((n-1)*n)/2)

if n%2 == 1:
    print('{}/{}'.format(n-c,c+1))

else:
    print('{}/{}'.format(c+1,n-c))