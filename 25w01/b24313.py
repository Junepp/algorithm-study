"""
O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
함수 f(n) = a1n + a0, 양의 정수 c, n0가 주어질 경우 O(n) 정의를 만족하는지 알아보자.
입력
첫째 줄에 함수 f(n)을 나타내는 정수 a1, a0가 주어진다. (0 ≤ |ai| ≤ 100)
다음 줄에 양의 정수 c가 주어진다. (1 ≤ c ≤ 100)
다음 줄에 양의 정수 n0가 주어진다. (1 ≤ n0 ≤ 100)

출력
f(n), c, n0가 O(n) 정의를 만족하면 1, 아니면 0을 출력한다.

예제 입력 1 
7 7
8
1
예제 출력 1 
0
f(n) = 7n + 7, g(n) = n, c = 8, n0 = 1이다. f(1) = 14, c × g(1) = 8이므로 O(n) 정의를 만족하지 못한다.

예제 입력 2 
7 7
8
10
예제 출력 2 
1
f(n) = 7n + 7, g(n) = n, c = 8, n0 = 10이다. 모든 n ≥ 10에 대하여 7n + 7 ≤ 8n 이므로 O(n) 정의를 만족한다.
"""

def solver(a1, a0, c, n0) -> int:
    if a1 - c == 0:
        if a0 <= 0:
            return 1
        else:
            return 0
    
    elif a1 - c < 0:
        k = (-1) * a0 / (a1 - c)
        if k <= n0:
            return 1
        else:
            return 0
        
    else:
        return 0

        
        
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

answer = solver(a1, a0, c, n0)
print(answer)
