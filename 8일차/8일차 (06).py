# 입력받은 리스트 안에 입력받은 문자열이 있으면 'True'를, 없으면 'False'를 출력하는 코드

a = int(input())
str = [input() for i in range(a)]
a = input()

if a in str:
    print(True)
else:
    print(False)
