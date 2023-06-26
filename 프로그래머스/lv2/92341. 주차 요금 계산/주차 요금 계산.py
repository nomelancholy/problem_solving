from collections import defaultdict
from datetime import datetime
import math

def solution(fees, records):
    answer = []
    
    basic_time, basic_fee, time_range, time_fee = fees
    
    parking_dict = defaultdict(list)
    car_time_stack = defaultdict(list)
    fee_dict = defaultdict(int)
    car_minute_dict = defaultdict(int)
    
    for record in records:
        time, car_number, status = record.split()
        parking_dict[car_number].append((status, time))
    
    for car_number, infos in parking_dict.items():
        for status, time in infos:
            if status == 'IN':
                car_time_stack[car_number].append(time)
            else:
                in_time = car_time_stack[car_number].pop()
                time_diff = datetime.strptime(time, '%H:%M') - datetime.strptime(in_time, '%H:%M')
                diff_time_info = str(time_diff).split(':')
                minutes = int(diff_time_info[0]) * 60 + int(diff_time_info[1])
                car_minute_dict[car_number] += minutes
               
    for car_number, infos in car_time_stack.items():
        if infos:
            in_time = infos.pop()
            time_diff = datetime.strptime('23:59', '%H:%M') - datetime.strptime(in_time, '%H:%M')
            diff_time_info = str(time_diff).split(':')
            minutes = int(diff_time_info[0]) * 60 + int(diff_time_info[1])
            car_minute_dict[car_number] += minutes

    for car_number, minutes in car_minute_dict.items():
        if minutes <= basic_time:
            fee_dict[car_number] += basic_fee
        else:
            cost = basic_fee   
            cost += math.ceil((minutes - basic_time) / time_range) * time_fee
            fee_dict[car_number] += cost         
        
    
    for k, v in sorted(fee_dict.items()):
        answer.append(v)
        
    return answer