def solution(data, ext, val_ext, sort_by):
    answer = []
    
    INDEX_DICT = { 'code' : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    
    ext_index = INDEX_DICT[ext]
    sort_index = INDEX_DICT[sort_by]
    
    answer = [arr  for arr in data if arr[ext_index] < val_ext]
    answer.sort(key=lambda x:x[sort_index])
    
    return answer