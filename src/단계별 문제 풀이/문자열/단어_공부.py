s = input().upper()
s_list = list(map(str,s))
s_set = set(s_list)
dic = {}
n_list = []
for c in s_set:
    sc = s_list.count(c)
    dic[sc] = c
    n_list.append(sc)
if n_list.count(max(dic.keys())) > 1:
    print('?')
else:
    print(dic[max(dic.keys())])










