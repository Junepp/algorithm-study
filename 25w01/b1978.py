"""
241231
N개 중에서 소수가 몇 개
입력: 첫 줄에 수의 개수 N (<=100) 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
출력: 주어진 수들 중 소수의 개수를 출력한다.

입력:
4
1 3 5 8

출력: 3
"""

_ = input()
inputs = list(map(int, input().split()))

ceil = max(inputs)
isPrime = [True for _ in range(ceil+1)]

for n in range(ceil+1):
    if n <= 1:
        isPrime[n] = False
        continue
    
    if not isPrime[n]:
        continue
    
    for x in range(1, ceil // n):
        rm_idx = n * (x + 1)
        isPrime[rm_idx] = False

answer = 0
for each in inputs:
    if isPrime[each]:
        answer += 1
    
print(answer)
