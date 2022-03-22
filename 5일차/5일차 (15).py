# 리스트를 입력받은 후 enumerate() 함수를 사용하여 인덱스와 그 인덱스 속 값을 출력하는 코드

a = int(input())

strs = [input() for str in range(a)]

print (strs)

for i, j in enumerate(strs):
    print (i, j)
