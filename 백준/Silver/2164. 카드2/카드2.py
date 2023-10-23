# 1~n 까지의 번호의 카드가 있다,
# 1번 카드가 제일 위, n번 카드가 제일 아래
# 제일 위에 있는 카드를 바닥에 버린다
# 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 카드가 한 장 남을때 까지 반복
from collections import deque

n = deque(range(1, int(input())+1,))
while len(n) != 1:
    n.popleft()
    n.rotate(-1)
print(n[0])