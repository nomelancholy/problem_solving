def solution(id_pw, db):
    answer = 'fail'
    
    id = id_pw[0]
    pw = id_pw[1]
    
    for info in db:
        if id == info[0]:
            answer = 'wrong pw'
            if pw == info[1]:
                answer = 'login'
                break
    
    return answer