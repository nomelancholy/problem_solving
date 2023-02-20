def solution(n):
    answer = ''
    
    # 숫자  3개 존재
    numbers = [1, 2, 4]
    
    # n이 3 보다 작아질 때 까지 반복
    while n > 3:

        # 값을 3으로 나눈 몫과 나머지를 구한다
        v, r = divmod(n, 3)
        
        # 몫은 n의 값으로 넣고
        n = v
        
        # 나머지는 index 로 활용해 해당 값을 찾아 넣는다
        answer += str(numbers[r - 1])
        
        # 만약 마지막으로 추가한 값이 4여서 한자리 올려야 하는 상황이면
        if answer[-1] == '4':
            print(n)
            # 나눗셈 인덱스가 제대로 작동할 수 있게 n을 1 줄여준다
            n -= 1
            
    answer += str(numbers[n - 1])
    
    # 거꾸로 출력
    answer = answer[::-1]
    
    return answer