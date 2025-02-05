N, M = map(int, input().split())

arr1 = []
arr2 = []
answer = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    line = list(map(int, input().split()))
    arr1.append(line)
    
for _ in range(N):
    line = list(map(int, input().split()))
    arr2.append(line)

for r in range(N):
    for c in range(M):
        answer[r][c] = arr1[r][c] + arr2[r][c]

for line in answer:
    for each in line:
        print(each, end=' ')
    print()
    