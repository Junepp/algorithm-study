ARR_SIZE = 9

arr = []
for _ in range(ARR_SIZE):
    line = list(map(int, input().split()))
    arr.append(line)
    
max = -1
for r in range(ARR_SIZE):
    for c in range(ARR_SIZE):
        if arr[r][c] > max:
            max = arr[r][c]
            coords = (r+1, c+1)

print(max)
print(coords[0], coords[1])
