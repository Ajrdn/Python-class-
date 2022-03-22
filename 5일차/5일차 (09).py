# 입력받은 리스트를 오름차순과 내림차순으로 정렬하여 출력하는 코드

strs = []
a = int(input())

for i in range(a):
    str = input()
    strs.append(str)

print (strs)
    
strs.sort()

print (strs)

strs.sort(reverse = True)

print (strs)
