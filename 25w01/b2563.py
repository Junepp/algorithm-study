"""
241230

전체면 100*100
한장 10*10

input:
3
3 7
15 7
5 2

output: 260
"""
FIELD_SIZE = 100
PAPER_SIZE = 10

arr = [[0 for _ in range(FIELD_SIZE+1)] for _ in range(FIELD_SIZE+1)]

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    
    arr[x][y] += 1
    arr[x][y+PAPER_SIZE] += -1
    arr[x+PAPER_SIZE][y] += -1
    arr[x+PAPER_SIZE][y+PAPER_SIZE] += 1

for x in range(FIELD_SIZE):
    for y in range(FIELD_SIZE):
        arr[x][y+1] += arr[x][y]

for y in range(FIELD_SIZE):
    for x in range(FIELD_SIZE):
        arr[x+1][y] += arr[x][y]

answer = 0
for each_l in arr[:-1]:
    for each in each_l[:-1]:
        if each:
            answer += 1

print(answer)
