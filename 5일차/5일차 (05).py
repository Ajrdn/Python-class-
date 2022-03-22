# 입력받은 리스트의 입력받은 인덱스의 요소를 삭제하는 코드

strs = []
a = int(input())

for i in range(a):
    str = input()
    strs.append(str)

print(strs)

a = int(input())

strs.pop(a)

print (strs)
