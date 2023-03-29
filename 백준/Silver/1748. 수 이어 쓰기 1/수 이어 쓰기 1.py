n = int(input())
n_length = len(str(n))

answer = 0

for digit in range(1, n_length + 1):
    if digit == n_length:
        this_digit_num_count = n - (10 ** (digit - 1) - 1)
        answer += this_digit_num_count * digit
    else:
        answer += 9 * (10**(digit - 1)) * digit

print(answer)