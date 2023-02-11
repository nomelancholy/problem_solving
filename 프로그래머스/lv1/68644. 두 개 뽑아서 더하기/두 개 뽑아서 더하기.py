def solution(numbers):
    
    sums = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            sums.append(numbers[i] + numbers[j])
            
    answer = list(set(sums))
    answer.sort()
    
    return answer