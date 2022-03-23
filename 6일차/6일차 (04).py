# 딕셔너리를 입력받은 뒤 Key값을 입력받아 해당 Key에 해당하는 value를 출력하는 코드

dt = {}
a = int(input())

for i in range(a):
    key = input()
    value = input()
    dt[key] = value

print(dt)

a = input()

print(dt[a])
