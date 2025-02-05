"""
250102

Equilateral :  세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우
단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다.
가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.

입력: 각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.
출력: 각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.

예제 입력 1 
7 7 7
6 5 4
3 2 5
6 2 6
0 0 0
예제 출력 1 
Equilateral
Scalene
Invalid
Isosceles
"""


def cls_process(legs) -> str:
    a, b, c = sorted(legs)

    if a == b == c == 0:
        return "Exit"
    
    if a + b <= c:
        return "Invalid"
    
    elif a == b == c:
        return "Equilateral"
    
    elif a == b or b == c:
        return "Isosceles"
    
    else:
        return "Scalene"

while True:
    legs = list(map(int, input().split()))

    tcls = cls_process(legs)
    
    if tcls == "Exit":
        break

    print(tcls)
    