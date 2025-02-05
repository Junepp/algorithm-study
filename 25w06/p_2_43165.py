"""
n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.

입출력 예
numbers	target	return
[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2

+4+1-2+1 = 4
+4-1+2-1 = 4
총 2가지 방법이 있으므로, 2를 return 합니다.
"""

# permute > 2**20 = 약 백만번 연산
# BFS

def solution(numbers, target):
    """
    테스트 1 〉	통과 (201.91ms, 34.7MB)
    테스트 2 〉	통과 (193.34ms, 34MB)
    테스트 3 〉	통과 (0.21ms, 10.2MB)
    테스트 4 〉	통과 (1.43ms, 10.4MB)
    테스트 5 〉	통과 (6.41ms, 10.9MB)
    테스트 6 〉	통과 (0.41ms, 10.1MB)
    테스트 7 〉	통과 (0.21ms, 10.3MB)
    테스트 8 〉	통과 (1.54ms, 10.5MB)
    """
    
    graph = [0]
    
    for i in numbers:
        new_graph = []
        
        while graph:
            now = graph.pop()
            new_graph.append(now + i)
            new_graph.append(now - i)
    
        graph = new_graph

    answer = graph.count(target)
    
    return answer

def solution(numbers, target):
    """
    테스트 1 〉	통과 (1.47ms, 10.2MB)
    테스트 2 〉	통과 (1.87ms, 10.2MB)
    테스트 3 〉	통과 (0.18ms, 10.2MB)
    테스트 4 〉	통과 (0.37ms, 10.2MB)
    테스트 5 〉	통과 (0.53ms, 10.2MB)
    테스트 6 〉	통과 (0.27ms, 10.1MB)
    테스트 7 〉	통과 (0.15ms, 10.2MB)
    테스트 8 〉	통과 (0.43ms, 10.1MB)
    """
    graph = {0: 1}
    
    for i in numbers:
        new_graph = {}
        
        for k, v in graph.items():
            n1 = k + i
            n2 = k - i
            
            if new_graph.get(n1) is None:
                new_graph[n1] = v
            else:
                new_graph[n1] += v
            
            if new_graph.get(n2) is None:
                new_graph[n2] = v
            else:
                new_graph[n2] += v
    
        graph = new_graph
    
    answer = graph[target] if graph.get(target) is not None else -1
    
    return answer

print(solution2([1 for _ in range(5)], 3))
