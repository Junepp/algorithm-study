"""
정수 n(0 ≤ n ≤ 4*(10**9))가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수

입력 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.
출력 각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.

예제 입력 1 
3
6
20
100
예제 출력 1 
7
23
101
"""
import sys

def isPrime(n):
    if n < 2:
        return False
        
    for share in range(2, int(n**0.5) + 1):
        if n % share == 0:
            return False
    
    else:
        return True

def getNextPrime(n):
    while True:
        if isPrime(n):
            return n

        n += 1
  
inputs = sys.stdin.readlines()
answer = []

for n in inputs[1:]:
    n = int(n.strip())
    answer.append(str(getNextPrime(n)))

print('\n'.join(answer))
