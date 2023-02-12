def solution(answers):
    
    # 찍는 방식 정의
    style = {1 : [1, 2, 3, 4, 5], 2 : [2, 1, 2, 3, 2, 4, 2, 5], 3 : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    
    scores = [0, 0, 0, 0]
    # 채점 
    for idx, answer in enumerate(answers):
        for i in range(1, 4):
            if style[i][idx % len(style[i])] == answer:
                scores[i] += 1
                
    # 최고점을 찾고
    best_count = max(scores)   
    
    # 그 점수를 획득한 학생을 배열에 추가
    best_students = []
    
    for i in range(1, len(scores)):
        if best_count == scores[i]:
            best_students.append(i)
            
    return best_students