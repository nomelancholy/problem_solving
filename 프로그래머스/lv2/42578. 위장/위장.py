from collections import defaultdict

def solution(clothes):
    answer = 1
    
    hash_dic = defaultdict(list)
    
    # 종류별로 세팅
    for cloth in clothes:
        hash_dic[cloth[1]].append(cloth[0])
        
    # 종류별로 경우의 수를 곱한다 (해당 종류 의상을 입지 않는 0의 경우 포함해서)
    for key, value in hash_dic.items():
        answer *= (len(value) + 1)
    
    # 한 종류의 의상도 입지 않은 경우를 빼서 return
    return answer - 1