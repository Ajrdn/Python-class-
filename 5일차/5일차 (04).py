# 입력받은 두 리스트를 더한 형태와 입력받은 수 만큼 곱한 형태를 출력하는 코드

strs = []
strs1 = []

a = int(input())

for i in range(a):
    str = input()
    strs.append(str)

a = int(input())

for i in range(a):
    str = input()
    strs1.append(str)

a = int(input())

print (strs + strs1)
print (strs * a)
print (strs1 * a)

