cnt = int(input()) # 입력 개수

str_set = set()  # 입력 문자열을 저장할 집합(set)
sorted_str_list = []
for i in range(cnt):
    str_set.add(input())

sorted_str_list = list(str_set)
sorted_str_list = (sorted(sorted_str_list, key=lambda x: (len(x), x)))
for k in sorted_str_list:
    print(k)