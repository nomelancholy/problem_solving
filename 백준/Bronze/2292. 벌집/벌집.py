n = int(input())


if n == 1:
  print(1)
else:
  room_range = 6 * (n -1)
  
  count = 1
  end_room = 1
  
  while True:
    count += 1
    
    room_range = 6 * (count - 1)
    end_room += room_range
  
    if n <= end_room:
      break
  
  print(count)