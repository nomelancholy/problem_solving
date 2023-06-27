from collections import defaultdict, deque

def solution(begin, target, words):
    answer = 0
    
    visited = {word:False for word in words}
    visited[begin] = True
    
    if target in words:
        q = deque([begin])
     
        while q:
            now = q.popleft()
            visited[now] = True
            answer += 1
            
            if now == target:
                answer -= 1
                break
            
            next_candidates = []
            
            for word in words:
                if visited[word]:
                    continue
                same_count = 0
                for i in range(len(now)):
                    if word[i] == now[i]:
                        same_count += 1
                if same_count == len(now) - 1:
                    next_candidates.append(word)
            
            next_same_count = 0
            next_word = ''
            for word in next_candidates:
                same_count = 0
                for i in range(len(target)):
                    if word[i] == target[i]:
                        same_count += 1
                if same_count > next_same_count:
                    next_word = word
            q.append(next_word)
            
    

    return answer