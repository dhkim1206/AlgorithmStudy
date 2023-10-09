# 1018
# M * N (8보다 크거나 같은) 크기의 정사각형, 규칙적이지 않음
# 8 * 8 크기로 잘라내어 정형화할 것이다.
# 지민이가 다시 칠해야 하는 정사각형의 최소 개수 출력
n, m = map(int, input().split())
board = []
min_changes = float('inf')

for _ in range(n):
    board.append(list(input()))

# 8x8 정사각형을 이동하면서 확인
for i in range(n - 7):
    for j in range(m - 7):

        repaint_cnt = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                # 첫 칸이 'W'일 때
                if (x + y) % 2 == 0:
                    if board[x][y] == 'B':
                        repaint_cnt += 1
                else:
                    if board[x][y] == 'W':
                        repaint_cnt += 1
        # 바둑 판을 그대로 놔두는 경우, 반대로 칠하는 경우 중 최소 값
        repaint_cnt = min(repaint_cnt, 64 - repaint_cnt)
        min_changes = min(min_changes, repaint_cnt, 64 - repaint_cnt)

print(min_changes)