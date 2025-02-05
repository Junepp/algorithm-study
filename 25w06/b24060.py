"""
N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 
병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 K 번째 저장되는 수를 구해서 우리 서준이를 도와주자.
0 5 6개
0 5
0
merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
    if (p < r) then {
        q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
        merge_sort(A, p, q);      # 전반부 정렬
        merge_sort(A, q + 1, r);  # 후반부 정렬
        merge(A, p, q, r);        # 병합
    }
}

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
merge(A[], p, q, r) {
    i <- p; j <- q + 1; t <- 1;
    while (i ≤ q and j ≤ r) {
        if (A[i] ≤ A[j])
        then tmp[t++] <- A[i++];
        else tmp[t++] <- A[j++];
    }
    while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
        tmp[t++] <- A[i++];
    while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
        tmp[t++] <- A[j++];
    i <- p; t <- 1;
    while (i ≤ r)  # 결과를 A[p..r]에 저장
        A[i++] <- tmp[t++]; 
}
입력
첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 500,000), 저장 횟수 K(1 ≤ K ≤ 108)가 주어진다.
다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

출력 배열 A에 K 번째 저장 되는 수를 출력한다. 저장 횟수가 K 보다 작으면 -1을 출력한다.

예제 입력 1 
5 7
4 5 1 3 2
예제 출력 1 
3

# 4 5 1 3 2 -> 4* 5 1 3 2 -> 4 5* 1 3 2 -> 1* 5 1 3 2 -> 1 4* 1 3 2 -> 1 4 5* 3 2 -> 1 4 5 2* 2 -> 1 4 5 2 3* -> 1* 4 5 2 3 -> 1 2* 5 2 3 -> 1 2 3* 2 3 -> 1 2 3 4 3 -> 1 2 3 4 5. 총 12회 저장이 발생하고 일곱 번째 저장되는 수는 3이다.
   

예제 입력 2 
5 13
4 5 1 3 2
예제 출력 2 
-1
"""

def merge_sort(unsorted_list, answer):
    arr_len = len(unsorted_list)
    
    if arr_len == 1:
        return unsorted_list
    
    bound = (arr_len + 1) // 2
    
    sorted_l = merge_sort(unsorted_list[:bound], answer)
    sorted_r = merge_sort(unsorted_list[bound:], answer)

    sorted_list = sorted_l + sorted_r
    sorted_list.sort()
    
    for each in sorted_list:
        answer.append(each)

    return sorted_list


N, K  = map(int, input().split())
arr = list(map(int, input().split()))

answer = []

merge_sort(arr, answer)

if len(answer) < K:
    print(-1)

else:
    print(answer[K-1])
