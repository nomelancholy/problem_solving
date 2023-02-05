def solution(bin1, bin2):
    answer = ''
    
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    
    answer = format(num1 + num2, 'b')
    
    return answer