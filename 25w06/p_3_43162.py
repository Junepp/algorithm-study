"""
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.

입출력 예
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
"""

def solution(n, computers):
    network = [-1 for _ in range(n)]  # 네트워크저장, 방문체크
    
    for cidx in range(n):
        # 네트워크에 포함되어 있는 경우
        if network[cidx] != -1:
            continue
        
        # 아직 네트워크가 없는 경우
        network[cidx] = cidx
        stack = [cidx]
        
        while stack:
            current = stack.pop()
            for target_idx, isConnect in enumerate(computers[current]):
                # 방문: 연결된 컴퓨터가 아직 네트워크 포함안된경우
                if isConnect == 1 and network[target_idx] == -1:
                    stack.append(target_idx)
                    network[target_idx] = cidx
    
    answer = len(set(network))
    
    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
