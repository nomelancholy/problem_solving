def solution(wallpaper):
    answer = []
    
    y_list = []
    x_list = []
    
    for y, line in enumerate(wallpaper):
        for x, point in enumerate(line):
            if point == '#':
                y_list.append(y)
                x_list.append(x)
    
    answer.append(min(y_list))
    answer.append(min(x_list))
    answer.append(max(y_list) + 1)
    answer.append(max(x_list) + 1)    
    
    return answer