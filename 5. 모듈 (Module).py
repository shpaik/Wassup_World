# module
from calculator import *

print(sum(3,5))
print(difference(5,3))

# randint & uniform
from random import randint, uniform     # random 모듈은 원래 깔려있음
print()
print(randint(1, 10))       # randint: 두 정수 사이의 랜덤 정수
print(uniform(0, 1))        # uniform: 두 수 사이의 랜덤한 소수

# input (user가 프로그램에 정보를 입력하는 것)
name = input("이름을 입력하세요: ")            # 입력받기전에 콘솔에 나옴. 설명용도
                                    # 실행하면 user가 입력할때까지 중단
                                    # 정한값으로 대채됨
                                    # 무조건 문자열로 대체
print("Hello " + name)

# 문자열 input을 int로 변환
volume = int(input("수량: "))
print("매출은 %d" % (volume * 3))
