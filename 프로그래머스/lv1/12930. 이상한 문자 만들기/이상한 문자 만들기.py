def solution(s):
    
    arr = s.split()
    
    chunk_arr = []
    
    for chunk in arr:
        new_chunk = ''
        for i, c in enumerate(chunk):
            if i % 2 == 0:
                new_chunk += c.upper()
            else:
                new_chunk += c.lower()
        chunk_arr.append(new_chunk)
    
    print(chunk_arr)
    
    characters = ''.join(chunk_arr)
    
    answer = ''
    
    index = 0
    
    for c in s:
        if c == ' ':
            answer += ' '
        else:
            answer += characters[index]
            index += 1
            
    return answer