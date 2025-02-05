"""
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
3: 스택에 들어있는 정수의 개수를 출력한다.
4: 스택이 비어있으면 1, 아니면 0을 출력한다.
5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)
둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.
출력을 요구하는 명령은 하나 이상 주어진다.

예제 입력 1 
9
4
1 3
1 5
3
2
5
2
2
5
예제 출력 1 
1
2
5
3
3
-1
-1
"""

import sys

inputs = sys.stdin.readlines()

stack = []
answer = []
for line in inputs[1:]:
    line = line.strip()
    command = line[0]
    
    if command == '1':
        x = line[2:]
        stack.append(x)
    
    elif command == '2':
        if stack:
            answer.append(stack.pop())
        else:
            answer.append('-1')
        
    elif command == '3':
        answer.append(str(len(stack)))
        
    elif command == '4':
        if stack:
            answer.append('0')
        else:
            answer.append('1')
            
    elif command == '5':
        if stack:
            answer.append(stack[-1])
        else:
            answer.append('-1')

print('\n'.join(answer))
