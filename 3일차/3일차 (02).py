# 입력받은 문자열을 다른 방식으로 출력하는 코드

a = input()
b = input()

print ('입력한 문자열 : %s, %s' % (a, b))
print (f'입력한 문자열 : {a}, {b}')
print ('입력한 문자열 : {0:s}, {1:s}'.format(a, b))
