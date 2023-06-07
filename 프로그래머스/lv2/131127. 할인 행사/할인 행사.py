def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9):

        flag = True
        want_dict = dict(zip(want, number))
        for item in discount[i: i + 10]:
            if item not in want_dict:
                flag = False
                break
            want_dict[item] -= 1
        if sum(want_dict.values()) == 0 and len(set(want_dict.values())) == 1:
            answer += 1        

    return answer