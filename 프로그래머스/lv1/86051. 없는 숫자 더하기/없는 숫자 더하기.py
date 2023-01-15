def solution(numbers):
    all_numbers = [i for i in range(10)]
    checked_list = list(set(all_numbers) - set(numbers))
    answer = 0
    answer += sum(checked_list)
    return answer