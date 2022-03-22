# 입력받은 리스트의 인덱스와 인덱스 속 값을 출력하는 코드

strs = []
a = int(input())

for i in range(a):
    str = input()
    strs.append(str)

print (strs)

for i in range(a):
    print (f'{i} : {strs[i]}')
