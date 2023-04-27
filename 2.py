
n, x = map(int, input('n x:').split())
num = list(map(int, input('숫자 n개를 입력하세요:').split()))

for i in range(n):
    if num[i] > x:
        print(num[i], end = " ")