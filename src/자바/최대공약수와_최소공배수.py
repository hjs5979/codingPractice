a,b = map(int, input().split())

n_list = []

for i in range(1,min(a,b)+1):
    if a%i == 0 and b%i == 0:
        n_list.append(i)

max_value = max(n_list)
print(max_value)
print(int((a/max_value) * b/max_value * max_value))
        
        