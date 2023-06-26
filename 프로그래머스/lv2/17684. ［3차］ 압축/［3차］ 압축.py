from collections import defaultdict

def solution(msg):
    answer = []
    
    dictionary = [chr(i + 64)for i in range(1, 27)]    
    longest_word_len = 1
    continue_index = []
        
    for i in range(len(msg)):
        if i in continue_index:
            continue
        for j in range(longest_word_len, 0, -1):
            if i + j > len(msg):
                continue
            if msg[i: i + j] in dictionary:
                for k in range(i, i + j):
                    continue_index.append(k)
                answer.append(dictionary.index(msg[i:i + j]) + 1)
                if i + j + 1 <= len(msg):
                    dictionary.append(msg[i:i + j + 1])
                    longest_word_len += 1
                break
                
    return answer