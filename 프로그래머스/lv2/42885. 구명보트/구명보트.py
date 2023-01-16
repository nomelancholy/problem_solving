from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort()
    waiting = deque(people)
    
    boat = []
    
    while waiting:
        # 보트가 비어있는 경우
        if not boat:
            human = waiting.pop()
            boat.append(human)            
        # 보트에 사람이 한명 타있는 경우
        else:
            if boat[0] + waiting[0] <= limit:
                human = waiting.popleft()
                boat.append(human)
            elif boat[0] + waiting[-1] <= limit:
                human = waiting.pop()
                boat.append(human)
            else:
                answer += 1
                boat = []
                human = waiting.pop()
                boat.append(human)
        if len(boat) == 2:
            answer += 1
            boat = []
            
        
    if boat:
        answer += 1
    
       
    return answer