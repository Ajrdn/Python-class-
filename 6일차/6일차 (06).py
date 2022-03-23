# 입력받은 딕셔너리의 입력받은 Key와 그에 해당하는 value를 삭제하는 코드

dt = {}
a = int(input())

for i in range(a):
    key = input()
    value = input()
    dt[key] = value

print(dt)

key = input()

del dt[key]

print(dt)

key = input()

dt.pop(key)

print(dt)
