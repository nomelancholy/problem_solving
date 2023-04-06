days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]

m, d = map(int, input().split())

total_days = 0

for i in range(m):
  total_days += dates[i]

total_days += (d - 1)

print(days[total_days % 7])