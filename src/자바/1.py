def check(number):
    answer = 1
    one = 0
    
    while True:
        
        one = one * 10 + 1
        if one % number == 0:
            return answer
        else:
            answer += 1
            
while True:
    try:
        n= int(input())
        print(check(n))
    except:
        break    





    
    