n = int(input())
s_cards = list(map(int, input().split()))
m = int(input())
m_cards = list(map(int, input().split()))

card_dict = {card: 1 for card in s_cards}

for m_card in m_cards:
  if card_dict.get(m_card):
    print(1, end= ' ')
  else:
    print(0, end= ' ')