def solution(nums):
    answer = 0
    
    # 데려갈 수 있는 폰켓몬의 수
    available_amount = len(nums) / 2
    
    # 선택할 수 있는 폰켓못늬 가짓수
    selection_numbers = len(set(nums))
    
    # 가짓수와 폰켓몬의 수에 따라 정답 선택
    answer = selection_numbers if available_amount >= selection_numbers  else available_amount
    
    return answer