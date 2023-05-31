x = int(input())

if x == 1:
    print('1/1')
else:
    count = 0
    length = 0
  
    for i in range(1, x + 1):
        count += i
        length = i
        if x <= count:
            break
          
    r = 0
    c = 0

    if length % 2 == 0:
        r = 1
        c = length
        
        for _ in range(count - length + 1, x):
            r += 1
            c -= 1      

    else:
        r = length
        c = 1

        for _ in range(count - length + 1, x ):
            r -= 1
            c += 1

    print(f'{r}/{c}')