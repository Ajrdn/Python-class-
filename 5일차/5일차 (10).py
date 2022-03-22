# 입력받은 리스트를 거꾸로 뒤집어 출력하는 코드

strs = []
a = int(input())

for i in range(a):
    str = input()
    strs.append(str)

print (strs)

strs.reverse()

print (strs)
