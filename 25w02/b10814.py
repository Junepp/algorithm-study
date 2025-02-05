"""
나이와 이름이 가입한 순서대로.
나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

입력
첫째줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
둘째줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다.
나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수
이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열

출력
첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순
나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력

예제 입력 1 
3
21 Junkyu
21 Dohyun
20 Sunyoung
예제 출력 1 
20 Sunyoung
21 Junkyu
21 Dohyun
"""
import sys

members = sys.stdin.readlines()[1:]
members = [mem.split()+[idx] for idx, mem in enumerate(members)]
members.sort(key=lambda x: (int(x[0]), x[2]))

for age, name, _ in members:
    print(age, name)
