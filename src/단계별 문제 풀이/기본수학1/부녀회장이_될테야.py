from msvcrt import kbhit


t = int(input())
apartment = []

for _ in range(t):
    k = int(input())
    n = int(input())
    
    a = [h for h in range(1,n+1)]
    apartment.append(a)


    for f in range(k):
        b = [sum(apartment[f][:h]) for h in range(1,n+1)]
        apartment.append(b)

    print(apartment)

    
    

    
