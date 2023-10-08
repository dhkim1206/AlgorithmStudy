# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때 까지 0의 개수를 구하는 프로그램 작성
def count_zeros_in_factorial(n):
    factorial = 1
    cnt = 0

    # 팩토리얼 계산
    for i in range(1, n + 1):
        factorial *= i

    # 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수 세기
    str_factorial = str(factorial)
    for k in reversed(str_factorial):
        if k == '0':
            cnt += 1
        elif k != '0':
            break
    return cnt

a = int(input())
result = count_zeros_in_factorial(a)
print(result)

