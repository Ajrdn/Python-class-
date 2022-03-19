# 입력받은 두 값의 사칙연산값을 (f-string)을 이용해 출력하는 코드

a = int(input('첫 번째 값 : '))
b = int(input('두 번째 값 : '))

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{b} - {a} = {b - a}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{b} / {a} = {b / a}')
print(f'{a} % {b} = {a % b}')
print(f'{b} % {a} = {b % a}')
