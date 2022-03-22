# 입력받은 리스트의 입력받은 인덱스 번호부터 입력받은 수까지와 입력받은 인덱스 번호부터 입력받은 수만큼 넘기며 출력하는 코드

strs = []
a = int(input())

for i in range(a):
    str = input()
    strs.append(str)

print (strs)

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
