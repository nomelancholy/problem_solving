from collections import defaultdict

def solution(score):
    
    answer = [0] * len(score)

    score_list = []
    score_dict = defaultdict(int)

    for i, s in enumerate(score):
        e = s[0]
        m = s[1]

        score_list.append((i, (e + m) / 2))
        score_dict[(e + m) / 2] += 1

    score_list.sort(key = lambda x : x[1], reverse=True)

    ranking = 1
    skip_count = 0
    
    for index, avg in score_list:
        
        answer[index] = ranking
        score_dict[avg] -= 1
        
        if score_dict[avg] != 0:
            skip_count += 1
        else:
            ranking += 1 + skip_count
            skip_count = 0
        
    return answer