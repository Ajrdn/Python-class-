# 입력받은 문자열과 리스트를 거꾸로 뒤집어 출력하는 코드

str = input()

print(str[::-1])
print (''.join(reversed(str)))
print(str.split(' ')[::-1])

str = list(str)
str.reverse()

print (''.join(str))
print(str[::-1])
