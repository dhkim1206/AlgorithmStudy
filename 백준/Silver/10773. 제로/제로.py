# 재민이 동아리 장부 관리
# 재현이도 재민이 도와서 돈 관리, 재현이는 항상 실수
# 재현이 : 잘못된 수를 부를 때 마다 0을 외쳐, 가장 최근에 재민이가 쓴 수를 지우게 한다
K = int(input())  # O(1) - 정수 하나를 입력받는 작업
klist = []  # O(1) - 빈 리스트를 초기화
ksum = 0  # O(1) - 정수 변수 초기화

for _ in range(K):
    value = int(input())  # O(K) - K번 반복해서 정수를 입력받음
    if value == 0:
        klist.pop()  # O(1) - 리스트의 가장 마지막 요소를 제거
    else:
        klist.append(value)  # O(1) - 리스트의 끝에 요소를 추가

for num in klist:
    ksum += num  # O(K) - 리스트의 모든 요소를 합산

print(ksum)
