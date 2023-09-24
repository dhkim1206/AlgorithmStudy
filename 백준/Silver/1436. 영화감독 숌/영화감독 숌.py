# 영화 개수
movie_cnt = int(input())

cnt = 0 # 일치하는 횟수
base = 666

# 666 1666 2666 3666 4666 5666 6666 7666|6660
# 부르투 포스 알고리즘
while(True):
    if "666" in str(base): #base에 666이 있다면
        cnt += 1 # cnt 1 증가
    if cnt == movie_cnt: # cnt가 영화 개수와 같다면
        print(base) 
        break
    base += 1



