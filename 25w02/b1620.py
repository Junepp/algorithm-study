"""
첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M
N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수

둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와. 
포켓몬의 이름은 모두 영어로만 이루어져있고, 첫 글자만 대문자이고, 나머지 문자는 소문자
일부 포켓몬은 마지막 문자만 대문자일 수도 있어. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2야.

그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와.
입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고, 
입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져. 그럼 화이팅!!!

출력
첫째 줄부터 차례대로 M개의 줄에 각각의 문제에 대한 답
숫자 > 이름을, 문자 > 이름에 해당하는 번호를 출력

예제 입력 1 
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna

예제 출력
Pikachu
26
Venusaur
16
14
"""

import sys

inputs = sys.stdin.readlines()
inputs = [line.strip() for line in inputs]

N, M = map(int, inputs[0].split())

number_name_list = inputs[1:N+1]
name_number_dict = {name: str(idx+1) for idx, name in enumerate(number_name_list)}

answer = []
for q in inputs[N+1:]:
    if q.isdigit():
        a = number_name_list[int(q)-1]
        answer.append(a)
    
    else:
        a = name_number_dict[q]
        answer.append(a)

answer = '\n'.join(answer)

print(answer)
