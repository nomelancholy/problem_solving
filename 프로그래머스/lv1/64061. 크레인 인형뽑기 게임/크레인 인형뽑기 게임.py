def solution(board, moves):
    answer = 0
    
    machine = []
    
    box = []
    
    # 일단 zip 활용해 묶고
    for tuple_pack in zip(*board):
        # 0 제거해 거꾸로 추가
        arr = [t for t in tuple_pack if t != 0]
        arr.reverse()
        machine.append(arr)
    
    # 집은 위치 순서대로 순회
    for move in moves:
        # 인형 집어 올리기 시도하는데
        # 비어 있으면
        if not machine[move - 1]:
            # 다음
            continue
        # 아니면 집어 올려서
        doll = machine[move - 1].pop()
        # 박스가 비어 있거나 맨 위 칸이 같은 인형이 아니면
        if not box or box[-1] != doll:
            # 그냥 인형 추가
            box.append(doll)
        # 집은 인형과 박스 맨 위칸이 같은 인형이면
        elif box[-1] == doll:
            # 펑~
            box.pop()
            answer += 2
            
    return answer