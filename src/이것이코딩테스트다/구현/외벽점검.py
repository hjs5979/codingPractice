from itertools import permutations
n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]

length = len(weak)

for i in range(length):
    weak.append(n+weak[i])

answer = len(dist) + 1

for start in range(length): # 0123
    for friends in list(permutations(dist, len(dist))):
        count = 1
        position = weak[start] + friends[count - 1]
        for index in range(start, start+length): # 0~3 / 1~4 / 2~5 / 3~6
            if position < weak[index]:
                count += 1
                if count > len(dist):
                    break
                position = weak[index] + friends[count-1]
        answer = min(answer, count)
if answer > len(dist):
    print(-1)
print(answer)