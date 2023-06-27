def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        time = 0
        roop_end = True
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                time += 1
            else:
                time += 1
                break
        answer[i] = time
        
    return answer