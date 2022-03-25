# 생성된 튜플 안에 입력받은 문자열이 있으면 'True'를, 없으면 'False'를 출력하는 코드

str1 = input()
str2 = input()
str3 = input()
str4 = input()
str5 = input()
tp = (str1, str2, str3, str4, str5)

a = input()

if a in tp:
    print(True)
else:
    print(False)
