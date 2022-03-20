# 입력받은 문자열을 입력받은 인덱스 번호부터 입력받은 수만큼 넘기며 출력하는 코드

str = input()
a = int(input())
b = int(input())

print (str[a::b])
print (str[b::a])
print (str[a::])
print (str[::a])
print (str[b::])
print (str[::b])
