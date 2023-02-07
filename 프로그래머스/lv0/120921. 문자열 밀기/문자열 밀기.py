def solution(A, B):
    answer = -1
    
    time = 0
    
    while time < len(B):
        if A == B:
            answer = time
            break
        A = A[-1] + A[:-1]
        time += 1
    
    return answer