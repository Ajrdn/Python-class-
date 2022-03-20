# 입력받은 수를 다양한 형태로 출력하는 코드

a = int(input('정수 입력 : '))

print (f'{a}')
print (f'{a : 5d}')
print (f'{a : 05d}')

a = float(input('실수 입력 : '))

print (f'{a}')
print (f'{a : 7.4f}')
print (f'{a : 07.4f}')


a = int(input('진수로 전환할 정수 입력 : '))
print (f'{a} {a : o} {a : x}')
