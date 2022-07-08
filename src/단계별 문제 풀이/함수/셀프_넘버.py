n_list = []
for i in range(1,10001):
    if i < 10:
        n_list.append(i+i)
    else:
        n = [int(number) for number in str(i)]
        n_list.append(i + sum(n))  
myset = set(range(1,10001))-set(n_list)
answer = list(myset)
answer.sort()
for i in answer:
    print(i)

