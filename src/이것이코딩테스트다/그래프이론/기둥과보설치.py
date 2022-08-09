n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

answer = []

for build in build_frame:
    x, y, a, b = build
    if b == 1:
        answer.append((x,y,a))
        possible(answer)
    
    if b== 0:
        answer.remove((x,y,a))
        