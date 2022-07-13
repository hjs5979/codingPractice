# a,b = map(int,input().split())
# print(a+b)

def recur(l): 
    c = 0
    for i in range(len(l)-1,0,-1):
        if ab_list[i] >= 10:
            ab_list[i] -= 10
            ab_list[i-1] += 1
            c+=1
    if c == 0:
        return l
    else:
        recur(l)

a,b = map(str,input().split())

m = max(len(a),len(b))

a = a.zfill(m)
b = b.zfill(m)

a_list = [int(i) for i in a]
b_list = [int(i) for i in b]

ab_list = [a_list[i] + b_list[i] for i in range(m)]

recur(ab_list)

answer = ''.join(map(str,ab_list))
print(answer)

