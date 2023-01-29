w = input()

def right(w):
    standard = 0
    for i in w:
        if i == "(":
            standard += 1
        else:
            standard -= 1
        
        if standard <= -1:
            return False
    return True

def balance(w):
    standard = 0
    for i in w:
        if i == "(":
            standard += 1
        else:
            standard -= 1
        
        if standard == 0:
            return True

def reverse(w):
    for i in range(len(w)):
        if w[i] == '(':
            w[i] = ')'
        else:
            w[i] = '('
    return w

def division(w):
    answer = ''
    if w == '':
        return w
    for i in range(2,len(w)+1,2):
        # print(i)
        # u = w[:i]
        # v = w[i:]
        # print(u,v)
        
        if balance(w[:i]) == True:
            u = w[:i]
            v = w[i:]
            break

    if right(u) == True:
        
        answer = u + division(v)
        
    else:
        answer = '('
        answer += division(v)
        answer += ')'
        
        # print(u)
        ud = list(u[1:-1])
        # print(ud)
        rud = reverse(ud)
        answer += "".join(rud)
        
    return answer

# def main(w):
    
#     u,v = division(w)
    
#     if right(u) == True:
#         division(v)

#     else:
#         ud = u[1:-1]
#         rud = reverse(ud)
#         blank = '(' + division(v) + ')' + rud
        
#         return blank
# print(reverse(')('))
print(division(w))
        