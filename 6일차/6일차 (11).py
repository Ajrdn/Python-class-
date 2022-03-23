# 입력받은 딕셔너리의 Key와 value를 함께 출력하는 코드

dt = {}
a = int(input())

for i in range(a):
    key = input()
    value = input()
    dt[key] = value

print(dt)

for i in dt.items():
    print(i)
