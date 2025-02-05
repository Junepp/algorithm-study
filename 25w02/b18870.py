"""
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

제한
1 ≤ N ≤ 1,000,000
-109 ≤ Xi ≤ 109

입력 1 
5
2 4 -10 4 -9
출력 1 
2 3 0 3 1

입력 2 
6
1000 999 1000 999 1000 999
출력 2 
1 0 1 0 1 0
"""

_ = int(input())
input = list(map(int, input().split()))

# coords = {}
# for each in input:
#     if coords.get(each) is not None:
#         coords[each] += 1
#     else:
#         coords[each] = 1

# sorted_keyset = list(coords.keys())
coords = list(set(input))
coords.sort()

answer = {}
for idx, each in enumerate(coords):
    answer[each] = idx

for each in input:
    print(answer[each], end=' ')

# sorted_keyset = coords
# sorted_keyset.sort()

# answer = {}
# prefix_sum = 0
# for k in sorted_keyset:
#     answer[k] = prefix_sum
#     prefix_sum += coords[k]

# for each in input:
#     print(answer[each], end=' ')
    
# orderd_coords = list(set(coords))
# orderd_coords.sort()

# cache = {}
# result = []

# for each in coords:
#     if cache.get(each) is not None:
#         idx = cache[each]
#     else:
#         idx = orderd_coords.index(each)
#         cache[each] = idx

#     result.append(idx)

# for each in result:
#     print(each, end=' ')
