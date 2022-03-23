# 입력받은 딕셔너리의 Key들과 value들을 따로, Key와 value를 묶어서 출력하는 코드

dt = {}
a = int(input())

for i in range(a):
    key = input()
    value = input()
    dt[key] = value

print(dt)
print(dt.keys())
print(dt.values())
print(dt.items())
