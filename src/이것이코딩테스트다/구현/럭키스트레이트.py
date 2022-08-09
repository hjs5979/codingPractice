s = list(map(int,input()))

half = int(len(s)/2)

left = 0
right = 0

for i in range(half):
    left += s[i]

for i in range(half,len(s)):
    right += s[i]
    
if left==right:
    print('LUCKY')
else:
    print('READY')