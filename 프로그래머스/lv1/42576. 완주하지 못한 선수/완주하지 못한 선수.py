import collections

def solution(participant, completion):

    c = collections.Counter(completion)
    for p in participant:
        if c[p] == 0:
            return p
        else:
            c[p] -= 1

#     participant.sort()
#     completion.sort()
    
#     answer = ''
    
#     for i, c in enumerate(completion):
#         if c != participant[i]:
#             answer = participant[i]
#             break
        
#         if i == len(completion) - 1:
#             answer = participant[i + 1]
        
#     return answer