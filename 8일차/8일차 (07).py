# 입력받은 딕셔너리 안에 입력받은 문자열이 있으면 'True'를, 없으면 'False'를 출력하는 코드

str = {}
a = int(input())

for i in range(a):
    key = input()
    value = input()
    str[key] = value

a = input()

if a in str or a in str.values():
    print(True)
else:
    print(False)
