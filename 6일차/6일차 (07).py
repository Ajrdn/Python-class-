# 입력받은 딕셔너리를 Key 기준 정렬, value 기준 정렬, Key, value를 함께 정렬하여 출력하는 코드

dt = {}
a = int(input())

for i in range(a):
    key = input()
    value = input()
    dt[key] = value

print(dt)

print(sorted(dt.keys()))
print(sorted(dt.values()))
print(sorted(dt.items()))
