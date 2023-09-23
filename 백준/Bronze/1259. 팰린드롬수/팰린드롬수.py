while(True):
    num = list(input())
    if(num[0]=="0"):
        break
    if num == num[::-1]:  # 문자열을 뒤집어서 팰린드롬 여부 확인
        print("yes")
    else:
        print("no")
