# permutation with recursive
def permutation(nodes):
    if len(nodes) == 1:
        return [nodes]
    
    permutes = []
    for nidx, current_node in enumerate(nodes):
        remain_nodes = nodes[:nidx] + nodes[nidx+1:]
        
        sub_permutes = permutation(remain_nodes)
        for sub_p in sub_permutes:
            permutes.append([current_node] + sub_p)
    depths_
    return permutes

nodes = [i for i in range(1, 4)]
permute = permutation(nodes)

for p in permute:
    print(p)

# divmod operator
share, remain = divmod(16, 3)
print(share, remain)

# binary operator
print(5 << 3)
print(bin(5))
print(int("1101", 2))
