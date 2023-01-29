n = int(input())

scores = [[] for _ in range(n)]

# print(scores)

for i in range(n):
    a,b,c,d = input().split()
    scores[i].append(a)
    scores[i].append(int(b))
    scores[i].append(int(c))
    scores[i].append(int(d))

scores.sort(key = lambda x:(-x[1], x[2], -x[3], x[0]))

for score in scores:       
    print(score[0])
