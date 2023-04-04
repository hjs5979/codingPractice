string = input()

answer = len(string)

for i in range(1,len(string)//2 + 1):
    comp = ''
    prev = string[0:i]
    count = 1
    for j in range(i,len(string),i):
        
        if prev == string[j:j+i]:
            count+=1
        
        else:
            comp += (str(count) + prev) if count > 1 else prev
            prev = string[j:j+i]
            count = 1
    # print(i,comp)
    comp += (str(count) + prev) if count > 1 else prev
    
    answer = min(answer,len(comp))

print(answer)