s = input()

s_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

answer = 0
for s1 in s:
    for i in s_list:
        if i.find(s1) != -1:
            answer += (s_list.index(i) + 3)

print(answer)
