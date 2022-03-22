# 입력받은 리스트의 입력받은 요소값을 삭제하는 코드

strs = []
a = int(input())

for i in range(a):
    str = input()
    strs.append(str)

print(strs)

str = input()

strs.remove(str)

print (strs)
