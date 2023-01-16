def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        sum_value = A[i] * B[i]
        answer += sum_value

    return answer