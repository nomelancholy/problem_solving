from collections import defaultdict

def solution(record):
    answer = []
    
    # 이름 
    uid_name_dict = defaultdict(str)
    
    # 메세지들 저장할 배열
    msgs = []
    
    for r in record:
        msg_list = r.split()
        
        if msg_list[0] == 'Leave':
            msgs.append('{}님이 나갔습니다.'.format(msg_list[1]))
        else:        
            # 들어오거나 이름을 변경할 경우 닉네임 저장
            uid_name_dict[msg_list[1]] = msg_list[2]
            
            if msg_list[0] == 'Enter':
                msgs.append('{}님이 들어왔습니다.'.format(msg_list[1]))
        
    for msg in msgs:
        # 해당 메세지의 uid 확인해서 그 uid의 최종 닉네임으로 대체한다
        first, _ = msg.split()
        uid = first[:-2]
        nickname = uid_name_dict[uid]
        
        answer.append(msg.replace(uid, nickname))
        

    return answer