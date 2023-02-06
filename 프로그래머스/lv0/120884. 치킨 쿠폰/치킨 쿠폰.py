def solution(chicken):
    answer = 0
    coupon = 0
  
    while chicken != 0:
        chicken -= 1
        coupon += 1
        if coupon == 10:
            chicken += 1
            answer += 1
            coupon = 0
    
    return answer