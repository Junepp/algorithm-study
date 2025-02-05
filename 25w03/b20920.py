"""
자주 나오는 단어일수록 앞에 배치한다.
해당 단어의 길이가 길수록 앞에 배치한다.
알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

M보다 짧은 길이의 단어의 경우 읽는 것만으로도 외울 수 있기 때문에 길이가 M이상인 단어들만 외운다고 한다. 

입력
첫째 줄에는 영어 지문에 나오는 단어의 개수 N과 외울 단어의 길이 기준이 되는 M이 공백으로 구분되어 주어진다.
(1 <= N <= 100,000, 1 <= M <= 10)

둘째 줄부터 N+1번째 줄까지 외울 단어를 입력받는다. 이때의 입력은 알파벳 소문자로만 주어지며 단어의 길이는 10을 넘지 않는다.
단어장에 단어가 반드시 1개 이상 존재하는 입력만 주어진다.

출력 화은이의 단어장에 들어 있는 단어를 단어장의 앞에 위치한 단어부터 한 줄에 한 단어씩 순서대로 출력한다.

예제 입력 1 
7 4
apple
ant
sand
apple
append
sand
sand
예제 출력 1 
sand
apple
append
예제 입력 2 
12 5
appearance
append
attendance
swim
swift
swift
swift
mouse
wallet
mouse
ice
age
예제 출력 2 
swift
mouse
appearance
attendance
append
wallet
"""

import sys

lines = sys.stdin.readlines()
N, M = map(int, lines[0].strip().split())

words = {}
for line in lines[1:]:
    line = line.strip()
    
    if len(line) < M:
        continue
    
    if words.get(line) is None:
        words[line] = 1
    
    else:
        words[line] += 1

keys = list(words.keys())
keys.sort(key=lambda x:(-words[x], -len(x), x))

print("\n".join(keys))
