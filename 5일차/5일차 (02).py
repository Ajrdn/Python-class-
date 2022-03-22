# 입력받은 수만큼 입력받은 리스트의 입력받은 인덱스 안에 값을 출력 후 입력받은 문자열을 추가하는 코드

strs = []
a = int(input())

for i in range(a):
    str = input()
    strs.append(str)

print (strs)

a = int(input())

print (strs[a])

str = input()

strs.insert(a, str)

print (strs)
