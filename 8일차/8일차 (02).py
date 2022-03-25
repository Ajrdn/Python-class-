# 입력받은 성적점수의 크기에 따른 점수를 출력하는 코드

x = float(input('점수입력 : '))

if x >= 90:
    print(f'성적 : {x}')
    print(f'등급 : A')
  
elif x >= 80 :
    print(f'성적 : {x}')
    print(f'등급 : B')

elif x >= 70 :
    print(f'성적 : {x}')
    print(f'등급 : C')

elif x >= 60 :
    print(f'성적 : {x}')
    print(f'등급 : D')

else :
    print(f'성적 : {x}')
    print(f'등급 : F')
