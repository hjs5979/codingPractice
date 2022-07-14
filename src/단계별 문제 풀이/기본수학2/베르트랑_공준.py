while True:
    a = int(input())
    if a == 0:
        break
    else:
        
        sieve = [True] * (2*a+1)

        m = int((2*a) ** 0.5) + 1

        for i in range(2, m):
            if sieve[i] == True:
                for j in range(i+i, 2*a+1, i):
                    sieve[j] = False

        p_list = [i for i in range(2, 2*a+1) if sieve[i] == True]
        
        answer = len([i for i in p_list if i > a])

        print(answer)