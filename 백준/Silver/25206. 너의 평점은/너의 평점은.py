total = 0
credit_total = 0

grade_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

for _ in range(20):
    title, credit, grade, = input().split()
    if grade == 'P':
        continue
    credit_total += int(float(credit))
    total = total + float(credit) * grade_dict[grade]
  
print(total / credit_total)