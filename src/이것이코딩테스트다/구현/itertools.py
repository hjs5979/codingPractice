from itertools import permutations, combinations, product, combinations_with_replacement

data = [1,2,3,4]

perm = list(permutations(data,3))

print(perm)

comb = list(combinations(data,2))

print(comb)

prod = list(product(data, repeat=2))

print(prod)

comb_r = list(combinations_with_replacement(data,2))
print(comb_r)

