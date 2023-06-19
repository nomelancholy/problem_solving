x, y = map(int, input().split())

x -= 1
y -= 1

n = max(x, y)

x_div, x_mod = divmod(x, 4)
y_div, y_mod = divmod(y, 4)

answer = 0

answer += max(x_div, y_div) - min(x_div, y_div)
answer += max(x_mod, y_mod) - min(x_mod, y_mod)

print(answer)