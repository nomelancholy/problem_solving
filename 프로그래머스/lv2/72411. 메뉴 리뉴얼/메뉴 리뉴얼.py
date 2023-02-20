from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    # 구성하고 싶어하는 갯수에 따라서 다르게 확인
    for c in course:
        # 주문들을 순회하는데
        
        # 일단 갯수 체크한 사전 자료형 하나 만들고
        count_dict = defaultdict(int)
        
        for order in orders:
            # 우선 가짓수보다 적게 시켰던 주문들은 제외
            if len(order) < c:
                continue
            
            # 글자는 앞 뒤 정렬하고
            order = sorted(order)
            # 갯수가 맞으면 조합 구성해서 순회
            for combi in combinations(list(order), c):
                count_dict[combi] += 1
        
        # 두 번 이상 주문된 조합이면
        if count_dict and max(count_dict.values()) > 1:
            # 가장 값이 큰 메뉴들 추출
            new_menu = [''.join(k) for k, v in count_dict.items() if max(count_dict.values()) == v]

        for menu in new_menu:
            answer.append(menu)
        
        answer = list(set(answer))
        
        answer.sort()
        
    return answer