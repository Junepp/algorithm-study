"""
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다.
그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.

예제 입력 1 
5
1
3
8
-2
2
예제 출력 1 
2
2
1
10
예제 입력 2 
1
4000
예제 출력 2 
4000
4000
4000
0
예제 입력 3 
5
-1
-2
-3
-1
-2
예제 출력 3 
-2
-2
-1
2
예제 입력 4 
3
0
0
-1
예제 출력 4 
0
0
0
1
"""

import sys

lines = sys.stdin.readlines()
N = int(lines[0])

if N == 1:
    n = int(lines[1])
    print(f"{n}\n{n}\n{n}\n0")

else:
    data = []
    cnt = {}
    for line in lines[1:]:
        """
        산술평균 : N개의 수들의 합을 N으로 나눈 값
        중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
        최빈값 : N개의 수들 중 가장 많이 나타나는 값
        범위 : N개의 수들 중 최댓값과 최솟값의 차이
        """
        n = int(line.strip())
        data.append(n)
        
        if cnt.get(n) is None:
            cnt[n] = 1
        else:
            cnt[n] += 1

    data.sort()
    cnt_key = list(cnt.keys())
    cnt_key.sort(key=lambda x: (cnt[x], -x), reverse=True)

    data_avg = round(sum(data)/len(data))
    data_mid = data[(len(data)-1)//2]
    data_most = cnt_key[1] if cnt[cnt_key[0]] == cnt[cnt_key[1]] else cnt_key[0]
    data_range = data[-1] - data[0]

    print(f"{data_avg}\n{data_mid}\n{data_most}\n{data_range}")
