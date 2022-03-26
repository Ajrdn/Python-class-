# 6개의 주사위 눈 중 무작위로 하나를 출력하는 코드

import random

def rolling_dice():
    n = random.randint(0x2680, 0x2685)
    print(chr(n))
    
rolling_dice()
