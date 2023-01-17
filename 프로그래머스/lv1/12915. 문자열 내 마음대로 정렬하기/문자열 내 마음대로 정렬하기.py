def solution(strings, n):
    
    # n번째 문자를 키로 hash를 구성한다
    n_hash = {}
    
    for string in strings:
        # 키가 없으면 배열 생성
        if string[n] not in n_hash.keys():
            n_hash[string[n]] = [string]
        # 키가 있으면 배열에 추가
        else:
            n_hash[string[n]].append(string)
    # 키 값을 기준으로 우선 정렬하고
    n_hash = sorted(n_hash.items())
    
    # 순회하며 내부의 배열을 사전순으로 다시 오름차순 정렬해 붙인다.
    answer = []
    
    for key, arr in n_hash:
        arr.sort()
        answer += arr
    
    return answer