a = int(input())

n = 0

first_num = a

while True:

    n+=1

    if a < 10:
        a = a*10 + a


    else:
        f = a%10
        s = a//10
        b = f + s
        a = f*10 + b%10

    if first_num == a:
        break

print(n)