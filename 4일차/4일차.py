# turtle 라이브러리를 다운받아 도형을 그리는 코드

import turtle as t

t.shape('turtle')

t.bgcolor('lightblue')

t.color('black')

while(1):
    a = int(input())
    if a > 0:
        l = int(input())
        g = 360 / a

        for i in range(a):
            t.fd(l)
            t.rt(g)

    elif a == 0:
        l = int(input())
        t.circle(100)

    else:
        break
        
