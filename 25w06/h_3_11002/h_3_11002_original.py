# import sys

# def bit_count(n):
#     count = 0
#     while n:
#         n &= n - 1
#         count += 1
#     return count

# def isKind(cpti_1, cpti_2):
#     diff_cnt = bit_count(cpti_1 ^ cpti_2)
    
#     if diff_cnt <= 2:
#         return 1
    
#     else:
#         return 0
    
# N, M = map(int, input().split())

# lines = sys.stdin.readlines()
# lines = [int(f'1{l.strip()}', 2) for l in lines]

# answer = 0

# for i in range(N):
#     cpti_1 = lines[i]
    
#     for j in range(i+1, N):
#         cpti_2 = lines[j]
#         result = isKind(cpti_1, cpti_2)

#         answer += result
        
# print(answer)


a = bin(37 ^ 1)
print(a)