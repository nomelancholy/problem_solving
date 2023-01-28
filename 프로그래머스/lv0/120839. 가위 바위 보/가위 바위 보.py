def solution(rsp):
    answer = ''
    
    win_dict = {'2':'0', '0':'5', '5':'2'}
 
    for s in rsp:
        answer += win_dict[s]

    return answer