from math import gcd

a_son, a_mom = map(int, input().split())
b_son, b_mom = map(int, input().split())

answer_son = a_son * b_mom + b_son * a_mom
answer_mom = a_mom * b_mom

mom_son_gcd = gcd(answer_son, answer_mom)

answer_son //= mom_son_gcd
answer_mom //= mom_son_gcd

print(answer_son, end=' ')
print(answer_mom)