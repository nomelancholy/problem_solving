def solution(numbers, hand):
    answer = ''
    
    left = [3, 0]
    right = [3, 2]
    
    pad = [[1,2,3], [4,5,6], [7,8,9], ['*', 0 , '#']]
    
    for number in numbers:
        for i, line in enumerate(pad):
            if number in line:
                j = line.index(number)
                if j == 0:
                    answer += 'L'
                    left = [i, j]
                elif j == 2:
                    answer += 'R'
                    right = [i, j]
                else:
                    # 가운데일 경우
                    # 떨어진 거리 계산 (- , abs)
                    left_distance = abs(i - left[0]) + abs(j - left[1])
                    right_distance = abs(i - right[0]) + abs(j - right[1])
                    
                    if left_distance > right_distance:
                        right = [i, j]
                        answer += 'R'
                    elif left_distance < right_distance:
                        left = [i, j]
                        answer += 'L'
                    else:
                        if hand == 'left':
                            left = [i, j]
                            answer += "L"
                        elif hand == 'right':
                            right = [i, j]
                            answer += "R"
        
    return answer