# 입력받은 두 리스트를 한 딕셔러니로 묶어 출력하는 코드

a = int(input())

strs1 = [input() for i in range(a)]
strs2 = [input() for i in range(a)]

strs = dict(zip(strs1, strs2))

print(strs)

strs = dict(zip(strs2, strs1))

print(strs)
