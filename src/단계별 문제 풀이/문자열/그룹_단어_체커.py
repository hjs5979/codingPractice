n = int(input())
answer = [1 for _ in range(n)]
for q in range(n):
    word = input()
    c = 0
    
    for a in range(len(word)):
        i = word[a:].find(word[a])
        # i2 = word[a+i+1:].find(word[a])

        # print(word[a], i, i2)
        if word[a+i+1:].find(word[a]) > 0:
            answer[q] = 0
# print(answer)
print(sum(answer))
     
        
            
    

         