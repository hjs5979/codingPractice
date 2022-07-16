n = int(input())
c = 0
for h in range(0,n+1):

    for m in range(0,60):

        for s in range(0,60):

            if '3' in (str(h) + str(m) + str(s)):
                c+=1

print(c) 

    