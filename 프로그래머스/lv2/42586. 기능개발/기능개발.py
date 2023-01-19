def solution(progresses, speeds):
    
    # stack으로 쓰기 위해 reverse
    progresses.reverse()
    speeds.reverse()

    count = 0
    
    answer = []
    # 남아있을 때는 반복
    while progresses:
        while progresses and progresses[-1] >= 100:
            count += 1
            progresses.pop()
        if count != 0:
            answer.append(count)
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
    
    return answer