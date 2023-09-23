# 과목 개수
cnt = int(input())

# 성적
before = list(map(int, input().split()))
after = []
top = max(before)

for i in before:
    after.append(i / top * 100)

# 조정된 점수 평균 계산
average = sum(after) / len(after)
print(average)