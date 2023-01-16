def solution(n, words):
    answer = []
    cache = []
    isFail = False
        
    for i, word in enumerate(words):
        # 비교 대상이 없을 경우는 스킵
        if not cache:
            cache.append(word)
            continue
        # 탈락인 케이스 (한글자, 중복, 끝말잇기 실패)
        if len(word) < 2 or word in cache or cache[-1][-1] != word[0]:
            return [i % n + 1, i // n + 1]
        
        cache.append(word)
    
    return [0, 0]