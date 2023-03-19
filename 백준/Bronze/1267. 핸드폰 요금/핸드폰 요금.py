y_charge = []
m_charge = []

n = int(input())

calls = list(map(int, input().split()))

for call in calls:
    y = 10 * (call // 30 + 1)
    m = 15 * (call // 60 + 1)

    y_charge.append(y)
    m_charge.append(m)
    
if sum(y_charge) > sum(m_charge):
    print('M', end=' ')
    print(sum(m_charge))
elif sum(y_charge) < sum(m_charge):
    print('Y', end=' ')
    print(sum(y_charge))
else:
    print(f'Y M {sum(m_charge)}')