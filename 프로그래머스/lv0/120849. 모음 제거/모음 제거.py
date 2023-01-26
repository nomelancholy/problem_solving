def solution(my_string):
    aeiou = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    
    for c in my_string:
        if c in aeiou:
            pass
        else:
            answer += c
    
    return answer