# 입력받은 딕셔너리의 Key들과 value들을 따로 리스트로 변환하여 출력하는 코드

dt = {}
a = int(input())

for i in range(a):
    key = input()
    value = input()
    dt[key] = value

print(dt)
print(list(dt.keys()))
print(list(dt.values()))
