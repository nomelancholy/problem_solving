from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = deque([])
    
    for city in cities:
        if city.lower() in cache:
            answer += 1
            cache.remove(city.lower())
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.popleft()
        
        cache.append(city.lower())
    
    return answer