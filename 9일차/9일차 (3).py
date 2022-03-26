# 입력받은 두 리스트에서 최솟값을 출력하는 코드

a = int(input())

nums = [int(input()) for i in range(a)]

print(min(nums))

a = int(input())

strs = [input() for i in range(a)]

print(min(strs))
