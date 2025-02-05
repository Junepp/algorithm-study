"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}

입력: 첫째 줄에 입력의 크기 n(1 ≤ n ≤ 500,000)이 주어진다.

출력: 첫째 줄에 코드1 의 수행 횟수를 출력한다.
둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

inputs:
7

outputs:
35
3

7
1 to 5
    i+1 to 6 
        j + 1 to 7
i= 1 15
    j 2 k 3~7 5
    j 3 k 4~7 4
    j 4 k 5~7 3
    j 5 k 6~7 2
    j 6 k 7~7 1 

i= 2 10
    j 3 k 4~7 4
    j 4 k 5~7 3
    j 5 k 6~7 2
    j 6 k 7~7 1
15 10 6 3 1  
"""
N = int(input())

cnt = (N-2)*(N-1)*N/6
cnt = round(cnt)

print(cnt)
print(3)
    