def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(v):
        visited[v] = True
        
        for index, computer in enumerate(computers[v]):
            if computer == 1 and not visited[index]:
                dfs(index)
        
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer