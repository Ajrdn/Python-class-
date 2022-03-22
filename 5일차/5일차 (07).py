# 입력받은 값의 입력받은 리스트 속 인덱스 값을 출력하는 코드

strs = []
a = int(input())

for i in range(a):
    str = input()
    strs.append(str)

print(strs)

str = input()

print (strs.index(str))
