def solution(money):
    v, r = divmod(money, 5500)
    answer = [v, r]
    return answer