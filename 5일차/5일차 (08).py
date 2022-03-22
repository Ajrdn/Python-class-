# 입력받은 값이 입력받은 리스트 안에 있는 개수를 출력하는 코드

strs = []
a = int(input())

for i in range(a):
    str = input()
    strs.append(str)

print(strs)

str = input()

print (strs.count(str))
