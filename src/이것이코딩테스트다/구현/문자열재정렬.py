s = input()

# s.sort()

string = []

number = 0

for i in s:
    try:
        number += int(i)
    except:
        string.append(i)
        
string.sort()

string.append(number)

for i in string:
    print(i, end='')
        
        
        
    
    