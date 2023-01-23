numbers = list(map(int,list(input())))

left = 0

right = 0

for i in range(len(numbers)):
    
    if i <= ((len(numbers)/2) - 1):
        left += numbers[i]
    else:
        right += numbers[i]
        
if left == right:
    print('LUCKY')
else:
    print('READY')

