n = int(input())

for i in range(n):
    n_list = list(map(int, input().split()))
    avg = sum(n_list[1:])/n_list[0]
    for i in range(n_list[0]):
        c = 0
        for s in n_list[1:]:
            if s > avg:
                c += 1
        
    print('{0:0.3f}%'.format(c/n_list[0]*100))
       