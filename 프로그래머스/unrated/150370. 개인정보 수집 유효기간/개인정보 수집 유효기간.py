from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    
    today_ymd = list(map(int, today.split('.')))
    terms_dict = defaultdict(int)
    
    for term in terms:
        term_pair = term.split(' ')
        terms_dict[term_pair[0]] = int(term_pair[1])
    
    for index, privacy in enumerate(privacies):
        privacy_pair = privacy.split(' ')
        privacy_date = list(map(int, privacy_pair[0].split('.')))
        privacy_type = privacy_pair[1]
        
        terms_dict[privacy_type]
        
        expiration_month = privacy_date[1] + terms_dict[privacy_type]
        expiration_date = []
        
        if expiration_month > 12:
            
            if expiration_month % 12 == 0:
                expiration_date.append(privacy_date[0] + expiration_month // 12 - 1)
                expiration_date.append(12)
            else:
                expiration_date.append(privacy_date[0] + expiration_month // 12)
                expiration_date.append(expiration_month % 12)
        else:
            expiration_date.append(privacy_date[0])
            expiration_date.append(expiration_month)
            
        expiration_date.append(privacy_date[2])
        
        expiration_flag = False
        
        ty = today_ymd[0]
        ey = expiration_date[0]
        tm = today_ymd[1]
        em = expiration_date[1]
        td = today_ymd[2]
        ed = expiration_date[2]
        
        if ty > ey:
            expiration_flag = True
        elif ty == ey:
            if tm > em:
                expiration_flag = True   
            elif tm == em:
                if td >= ed:
                    expiration_flag = True
        
        if expiration_flag:
            answer.append(index + 1)
            
    return answer