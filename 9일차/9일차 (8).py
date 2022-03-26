# 입력받은 두 수 사이의 수들 중 무작위로 하나를 출력하는 코드

import random

a = int(input())
b = int(input())

n = random.randint(a, b)

print(n)
