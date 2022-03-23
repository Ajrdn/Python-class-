# 입력받은 딕셔너리를 Key 기준 Key, value 함께 정렬한 것과 value 기준 Key, value 함께 정렬한 것을 출력하는 코드

import operator

dt = {}
a = int(input())

for i in range(a):
    key = input()
    value = input()
    dt[key] = value

print(dt)
print(sorted(dt.items(), key=operator.itemgetter(0)))
print(sorted(dt.items(), key=operator.itemgetter(1)))
