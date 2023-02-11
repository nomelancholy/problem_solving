from datetime import date

def solution(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    answer = date(2016, a, b).strftime('%a').upper()
    return answer