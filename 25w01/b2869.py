"""
241231
높이가 V미터인 나무 막대를 올라
달팽이는 낮에 A미터 올라. 자는 동안 B미터 미끄러.
정상에 올라간 후에는 미끄러지지 않는다.

입력: 세 정수 A, B, V가 공백으로 구분(1 ≤ B < A ≤ V ≤ 1,000,000,000)
출력: 달팽이가 나무 막대를 모두 올라가는데 며칠

input: 2 1 5
output: 4

input: 5 1 6
output: 2

input: 100 99 1000000000
output: 999999901

input: 999999999 999999998 1000000000
output: 2
"""

import math

A, B, V = map(int, input().split())

# (A - B) * answer + A = V
answer = math.ceil((V - A) / (A - B))
print(answer+1)
    