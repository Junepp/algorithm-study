import sys

N, M = map(int, input().split())
lines = sys.stdin.readlines()

cbtis = {}

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    int_form = int(line, 2)
    
    if cbtis.get(int_form) is None:
        cbtis[int_form] = 1
    
    else:
        cbtis[int_form] += 1

answer = 0

for k in list(cbtis.keys()):
    answer += (cbtis[k] * (cbtis[k]-1))
    
    for i in range(M):
        # 1개 다른
        k_diff1 = k ^ (1 << i)
        if cbtis.get(k_diff1) is not None:
            answer += cbtis[k] * cbtis[k_diff1]

        # 2개 다른
        for j in range(i+1, M):
            k_diff2 = k_diff1 ^ (1 << j)
            if cbtis.get(k_diff2) is not None:
                answer += cbtis[k] * cbtis[k_diff2]

print(answer // 2)
