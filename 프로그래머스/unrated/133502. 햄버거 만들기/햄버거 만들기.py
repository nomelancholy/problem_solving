def solution(ingredient):
    answer = 0
    recipe = [1, 2, 3, 1]
    desk = []
    
    for i in ingredient:
        desk.append(i)
        if len(desk) >= 4:
            if desk[-4:] == recipe:
                answer += 1
                del desk[-4:]
            
    return answer