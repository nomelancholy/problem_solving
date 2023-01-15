def solution(seoul):
    for i, c in enumerate(seoul):
        if c == 'Kim':
            return '김서방은 {}에 있다'.format(i)