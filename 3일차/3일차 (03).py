# 입력받은 수와 문자열의 위치를 바꿔서 출력하는 코드

a = int(input('첫번째 정수 : '))
b = int(input('두번째 정수 : '))

print (a, b)
a, b = b, a
print (a, b)

a = float(input('첫번째 실수 : '))
b = float(input('두번째 실수 : '))

print (a, b)
a, b = b, a
print (a, b)

a = input('첫번째 문자열 : ')
b = input('두번째 문자열 : ')

print (a, b)
a, b = b, a
print (a, b)
