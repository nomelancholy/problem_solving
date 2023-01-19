def solution(s):
    tuples = []
    
    # 앞 뒤의 겹괄호는 자른다
    s = s[1: -1]
    
    # 숫자 검색 모드 구분자
    isSearchingNumber = False
    
    # 숫자 받을 배열
    arr = []
    string = ''
    
    for c in s:
        # 괄호가 열리면 검색 모드 시작하고 배열 초기화
        if c == '{':
            isSearchingNumber = True
            arr = []
        # 괄호가 닫히면 검색 모드 종료하고 배열 튜플에 담음
        elif c == '}':
            isSearchingNumber = False
            
            # 만약 쉼표를 만나지 못하고 괄호가 닫혔으면 괄호 배열에 담고 문자열 초기화
            if string != '':
                arr.append(int(string))
                string = ''
            
            tuples.append(arr)
        # 쉼표를 만났을 때 
        elif c == ',':
            # 숫자와 숫자 사이 쉼표면
            if isSearchingNumber:
                arr.append(int(string))
                string = ''
            # 괄호랑 괄호 사이 쉼표면 그냥 넘어가고
            else:
                continue
        # 숫자를 만나면 string 에 더함
        else:
            string += c
            
    # 배열 길이 순으로 정렬
    tuples.sort(key=len)
    
    answer = []
    
    # tuples 순회하는데
    for t in tuples:
        # 원소들 살피면서
        for n in t:
            # 아직 정답 배열에 그 값이 없으면 추가
            if n not in answer:
                answer.append(n)
        
    
    return answer