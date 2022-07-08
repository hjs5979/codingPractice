import re

word = input()

c_list = re.findall('c=|c-|dz=|d-|lj|nj|s=|z=', word)
n = 0

for i in c_list:
    n += len(i)

print(len(word)  - n + len(re.findall('c=|c-|dz=|d-|lj|nj|s=|z=', word)))