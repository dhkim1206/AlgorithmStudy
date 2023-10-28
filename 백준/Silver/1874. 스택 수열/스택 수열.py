# 1 ~ n 까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써 하나의 수열 생성
# 이 때 push하는 순서는 반드시 오름차순
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지
# 있다면 어떤 순서로 push와 pop연산을 수행해야 하는지를 알아낼 수 있다.
# 이를 계산하는 프로그램을 작성

n = int(input())
start = 1
stack = []
operator = []
flag = 0

for _ in range(n):
    pop_num = int(input())
    # PUSH는 오름차순 순으로 해야하기 때문에
    # POP해야 할 숫자까지 값을 PUSH
    while start <= pop_num:
        stack.append(start)
        operator.append("+")
        start += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 POP
    if stack[-1] == pop_num:
        stack.pop()
        operator.append('-')

    # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
    # 예를 들어 12534일 경우 5를 POP하고 난 후, 스택의 맨 위는
    # 4이다, 3은 4의 아래에 있기 때문에 결국 4가 먼저 POP이 되어
    # 12543이 된다.
    # 12534는 될 수 없다.
    else:
        flag = 1
        print("NO")
        break

if flag == 0:
    for i in operator:
        print(i)

# 1,2,3,4,5,6,7,8
# ****************************
# 1,2,3,4   ++++
# 1,2,      --     4,3
# 1,2,5,6   ++           4,3
# 1,2,5     -          4,3,6
# 1,2,5,7,8, ++
#     x       -----   8,7,5,2,1
# ****************************
# 4,3,6,8,7,5,2,1
