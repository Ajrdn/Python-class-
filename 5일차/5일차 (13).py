# 이차원 리스트의 값을 하나씩 출력하는 코드

strs = [[1,2,3],[4,5,6],[7,8,9]]

print (strs)

for i in strs:
    for j in i:
        print (j)

print ('--------------')

for i in strs:
    for j in range(3):
        print (i[j])
