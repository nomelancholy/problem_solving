def solution(dartResult):
    answer = 0
    
    # 세 번의 점수를 계산할 배열
    each_score = []
    
    # 체크가 끝난 인덱스 저장
    checked_index = 0
    
    for i, c in enumerate(dartResult):
        # S, D, T 기준으로 자른다
        if c.isalpha():
            # 점수 확인하고
            score = int(dartResult[checked_index:i])
            
            # 제곱 값 곱한 다음
            if c == 'S':
                score = score ** 1
            elif c == 'D':
                score = score ** 2
            elif c == 'T':
                score = score ** 3
            
            # 인덱스 업데이트
            checked_index = i + 1
            
            # 뒤에 옵션이 있는지 확인해서 있으면
            if i + 1 < len(dartResult) and not dartResult[i + 1].isdigit():
                # 체크한 인덱스 업데이트 하고
                checked_index += 1
                # 스타상일 경우
                if dartResult[i + 1] == '*':
                    # 점수 2배 처리
                    score = score * 2
                    # 이전 점수가 있으면
                    if each_score:
                        # 이전 점수 2배 처리
                        each_score[-1] = each_score[-1] * 2
                # 아차상일 경우
                elif dartResult[i + 1] == '#':
                    score = score * -1
            # 계산이 끝났으니 각각의 점수를 기록하고
            each_score.append(score)
    # 합계를 return
    answer = sum(each_score)
    
    return answer