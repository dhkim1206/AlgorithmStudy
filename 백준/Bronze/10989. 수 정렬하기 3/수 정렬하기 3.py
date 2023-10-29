# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램 작성
import sys

N = int(input())  # O(1)

# 0부터 10000까지의 숫자를 저장하기 위한 리스트 (공간 복잡도: O(10001) ≈ O(1), 상수 크기)
n_list = [0] * 10001  # 10001개의 인덱스 리스트

for _ in range(N):
    num = int(sys.stdin.readline())
    n_list[num] += 1 # 입력된 숫자의 빈도수를 저장하기 위한 리스트 (공간 복잡도: O(1))

for i in range(len(n_list)):
    if n_list[i] != 0:
        for _ in range(n_list[i]):
            print(i)

# 총 공간 복잡도: O(1) + O(1) ≈ O(1)