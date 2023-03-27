n = int(input())
now_note = 0
answer = 0

while n != 0:
    answer += 1
    now_note += 1

    if n - now_note < 0:
        now_note = 1

    n -= now_note
    
print(answer)