n_list = []
for i in range(10):
    n_list.append(int(input())%42)

print(len(set(n_list)))