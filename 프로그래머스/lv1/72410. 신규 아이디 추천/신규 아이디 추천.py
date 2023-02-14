def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    
    SYMBOLS = ['-', '_', '.']
    
    # 2단계
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in SYMBOLS:
            answer += c
    
    new_id = ""
    
    # 3단계 
    # 한글자일 경우
    if answer and len(answer) == 1:
        new_id = answer
    # 아닐 경우
    else:
        for i in range(len(answer) - 1):
            if not (answer[i] == '.' and answer[i + 1] == '.'):
                new_id += answer[i]
            if i == len(answer) - 2 and not (answer[i + 1] == '.' and  answer[i] == '.'):
                new_id += answer[i + 1]
    

    
    # 4단계
    if new_id:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
   
    # 5단계
    if not new_id:
        new_id = 'a'
        
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
    # 6-1단계
    if new_id:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
            
    # 7단계
    if len(new_id) <= 2:
        length = 3 - len(new_id)
        for _ in range(length):
            new_id += new_id[-1]

    answer = new_id
    
    return answer