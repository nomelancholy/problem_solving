def solution(s, n):
    arr = [c if c == ' ' else ord(c) for c in s]
    
    print(arr)
    
    answer = ''
    
    for i in arr:
        # 공백
        if i == ' ':
            answer += i
        # 대문자
        elif 65 <= i <= 90:
            if i + n > 90:
                answer += chr(i + n - 90 + 64)
            else:
                answer += chr(i + n)
        # 소문자
        elif 97 <= i <= 122:
            if i + n > 122:
                answer += chr(i + n - 122 + 96)
            else:
                answer += chr(i + n)

            
    return answer