# 생성한 튜플의 입력받은 인덱스 번호부터 입력받은 수까지와 입력받은 인덱스 번호부터 입력받은 수만큼 넘기며 출력하는 코드

strs = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

a = int(input())
b = int(input())

print (strs[a:b])
print (strs[b:a])
print (strs[a:])
print (strs[:a])
print (strs[b:])
print (strs[:b])
print (strs[a::b])
print (strs[b::a])
print (strs[a::])
print (strs[::a])
print (strs[b::])
print (strs[::b])
