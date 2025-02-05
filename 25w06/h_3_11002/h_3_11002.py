import sys

def bit_count(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

def checkKind(cpti_1, cpti_2):
    diff_cnt = bit_count(cpti_1 ^ cpti_2)
    
    if diff_cnt <= 2:
        return 1
    
    else:
        return 0
    
# def checkKind(k1, k2):
#     bitwise_xor = k1 ^ k2

#     diff_cnt = 0
#     while bitwise_xor >= 1:
#         bitwise_xor, remain = divmod(bitwise_xor, 2)
#         diff_cnt += remain
        
#         if diff_cnt > 2:
#             return False
    
#     return True
    
N, M = map(int, input().split())
lines = sys.stdin.readlines()

cbtis = {}

for line in lines:
    line = line.strip()
    int_form = int(line, 2)
    
    if cbtis.get(int_form) is None:
        cbtis[int_form] = 1
    
    else:
        cbtis[int_form] += 1


keys = list(cbtis.keys())
answer = 0

for i in range(len(keys)):
    k1 = keys[i]
    for j in range(i, len(keys)):
        k2 = keys[j]
        
        if k1 == k2:
            answer += (cbtis[k1] * (cbtis[k1]-1)) // 2
            continue
        
        isKind = checkKind(k1, k2)
        
        if isKind:
            answer += (cbtis[k1] * cbtis[k2])

print(answer)
