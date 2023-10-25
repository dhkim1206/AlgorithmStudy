N = int(input())
A = set(map(int, input().split())) # set으로 시간 복잡도 줄이기 O(1)
M = int(input()) 
B = list(map(int, input().split())) # O(N)
for num in B:
    print(1) if num in A else print(0)