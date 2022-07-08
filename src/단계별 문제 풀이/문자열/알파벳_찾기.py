s = input()
a = 'abcdefghijklmnopqrstuvwxyz'
answer = []
for i in a:
    answer.append(s.find(i))
answer = list(map(str, answer))
answer = ' '.join(answer)
print(answer)
