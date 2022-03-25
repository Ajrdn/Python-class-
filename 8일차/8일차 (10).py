# 입력받은 리스트의 요소를 하나씩 출력하는 코드

a = int(input())
strs = [input() for i in range(a)]

for i in strs:
    print(i)
