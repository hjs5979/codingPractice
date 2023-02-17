n = 5

# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

# result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

def check(answer):
    for x,y,a in answer:
        if a == 0:
            if y==0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif a==1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1, y, 1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True
        
def solution(n, build_frame):
    answer = []
    
    for i in range(len(build_frame)):
        x,y,a,b = build_frame[i]

        if b == 1:
            answer.append([x,y,a])
            if check(answer) == False:
                answer.remove([x,y,a])

        else:
            answer.remove([x,y,a])
            if check(answer) == False:
                answer.append([x,y,a])
                
                

    return sorted(answer,key=lambda x:(x[0],x[1]))

solution(n,build_frame)