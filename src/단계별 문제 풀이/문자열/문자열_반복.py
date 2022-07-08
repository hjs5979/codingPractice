n = int(input())
for case in range(n):
    l, s = map(str,input().split())
    l = int(l)
    answer = ''
    for c in s:
        answer += c*l
    print(answer)
