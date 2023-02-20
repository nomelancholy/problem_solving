def solution(s):
    
    if len(s) == 1:
        return 1
    
    answer = 1001

    for token_len in range(1, int(len(s) / 2) + 1):
        token_text_arr = [s[token_point: token_point + token_len] for token_point in range(0, len(s), token_len)]

        current_word = token_text_arr[0]
        prefix_count = 1

        compressed_string = ''

        for pre, next in zip(token_text_arr, token_text_arr[1:] + ['']):
            if pre == next:
                prefix_count += 1
            else:
                if prefix_count != 1:
                    compressed_string += str(prefix_count)
                compressed_string += current_word
                current_word = next
                prefix_count = 1

        answer = min(answer, len(compressed_string))

    return answer