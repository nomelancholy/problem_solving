from itertools import permutations 

def solution(numbers):
   # 첫 시도
    # 들어온 숫자 리스트를 정수부가 한자리인 소수 형태로 변경하고, 복원을 위해 길이를 튜플로 함께 저장해 리스트 생성
    float_numbers = [(n * (1 / (10 ** (len(str(n)) - 1))), len(str(n))) for n in numbers]
    # 튜플의 첫번째 원소로 내림차순 정렬
    float_numbers.sort(key=lambda x:x[0], reverse=True)
    
    
#     # 정렬된 순서대로 원래 숫자로 복원하여 문자열 answer에 추가
    answer = ''
    
    for a, b in float_numbers:
        n = 0
        if b == 1:
            n = int(a)
        else:
            n = int(a * (10 * (b - 1)))
        
        answer += str(n)

    answer = ''
    
    numbers = [((str(n) * 4)[:4], len(str(n))) for n in numbers]
    numbers.sort(key=lambda x:x[0], reverse=True)
    
    for n, l in numbers:
        s = n[:l]
        answer += s
    
    if answer.count("0") == len(answer): 
        answer = "0"
    
    return answer

    # pms = list(permutations(numbers, len(numbers)))
    # candis = list(map(lambda tupl: ''.join([str(x) for x in tupl]), pms))
    # return max(candis)