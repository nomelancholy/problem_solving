def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_stack = list(reversed(list(skill)))
        skill_tree_list = list(skill_tree)
        
        flag = True
        
        for skill_t in skill_tree_list:
            if skill_t in skill_stack:
                if skill_t == skill_stack[-1]:
                    skill_stack.pop()
                else:
                    flag = False
                    break
            else:
                continue
                
        if flag:
            answer += 1
            
    return answer