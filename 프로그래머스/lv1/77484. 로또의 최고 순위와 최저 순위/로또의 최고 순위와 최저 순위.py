def draw(count):
    grade = 6
    
    if count == 6:
        grade = 1
    elif count == 5:
        grade = 2
    elif count == 4:
        grade = 3
    elif count == 3:
        grade = 4
    elif count == 2:
        grade = 5
    return grade
        

def solution(lottos, win_nums):
    
    min_count = 0
    
    # 확실히 맞은 번호는 두 배열 모두에서 삭제
    for lotto in lottos[:]:
        if lotto in win_nums:
            min_count += 1
            lottos.remove(lotto)
            win_nums.remove(lotto)
            
    max_count = min_count + lottos.count(0)

    print(max_count)
    print(min_count)
    
    answer = [draw(max_count), draw(min_count)]
    
    return answer