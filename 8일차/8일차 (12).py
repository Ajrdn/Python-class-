# 시작 수와 마지막 수를 입력받은 후 입력받은 문자열이 'even'이라면 시작 수와 마지막 수 사이의 짝수만 출력하고, 입력받은 문자열이 'odd'라면 시작 수와 마지막 수 사이의 홀수만 출력하는 코드

a = int(input('strat number : '))
b = int(input('end number : '))
nt = input('even or odd? : ')

if nt == 'even':
    i = a
    while i <= b:
        if i % 2 == 1:
            i += 1
            continue
        if i == b:
            print(i)
            break
        print(i, end=', ')
        i += 1

elif nt == 'odd':
    i = a
    while i <= b:
        if i % 2 == 0:
            i += 1
            continue
        if i == b:
            print(i)
            break
        print(i, end=', ')
        i += 1
