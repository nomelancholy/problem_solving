def solution(quiz):
    answer = []
    
    for q in quiz:
        qna = q.split('=')
        q = qna[0]
        a = qna[1]
        
        if eval(q) == int(a):
            answer.append('O')
        else:
            answer.append('X')
    
    return answer