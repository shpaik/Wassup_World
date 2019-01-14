# While 반복문: Loop
#  While 조건부분 (Boolean값):
#   수행부분 (반복적으로 실행하고 싶은 명령들
print("----------While----------")
# "I can cod too!" 3번 출력
i=1                         # i 초기값
while i <= 5:               # 조건부분, 다시 돌아오는 곳. i 는 3보다 작거나 같다
    print("I can code!")    # 수행부분
    i = i + 1               # i의 값을 1 늘려준다 (지정연산자, 같다는 의미가 아니다)

# 100까지의 짝수
print("--")
i = 2
while i <= 100:         # 원하는 값일때
    print(i)            # 출력
    i = i + 2

#100 이상의 23의 배수
print("--")
i = 100
while (i % 23) != 0:    # 원하는 값이 아닐때
    i = i + 1           # 다음을 검사
print(i)


# If 문: conditional
print("----------if----------")
# if 조건부분:
#       수행부분
# else:
#       수행부분

# 온도
temp = 15
if temp <= 10:
    print("자켓을 입는다.")
else:
    print("ㄴㄴ")


# elif 문 ( else + if)
print("----------elif----------")
온도 = 3
if 온도 <= 5:
    print("a+b+c+d")
elif 온도 <= 10:
    print("a+b+c")
elif 온도 <= 15:
    print("a+b")
else:
    print("a")


# 학점 계산기
def print_grade(midterm, final):
    total = midterm + final
    if total >= 90:
        print("You get an A")
    elif total >= 80:
        print("You get a B")
    elif total >= 70:
        print("You get a C")
    elif total >= 60:
        print("You get a D")
    else:
        print("You fail")
# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)

# 이상한 수학문제 1. 100 이하의 8의 배수이면서 12의 배수가 아닌 수들.
print("--")
i = 8
while i <= 100:
    if i % 12 != 0 and i % 8 == 0:
        print(i)
    i = i + 8

# 이상한 수학문제 2. 1000 보다 작은 자연수중 2 또는 3의 배수의 합
print("--")
i = 1
sum = 0                             # print대신에 sum을 정의후
while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        sum = sum + i
    i = i + 1
print(sum)                          # sum을 출력해야함

# 약수 찾기. 120의 약수의 개수
print()
n = 120
i = 1
count = 0
while i <= n:
    if n % i == 0:
        print(i)
        count = count + 1
    i = i + 1
print("%d의 약수는 %d개 입니다." % (n,count))

# 택이의 우승상금
print()
#Constant & Variables
INTEREST_RATE = 0.12
APT_PRICE = 1100000000
year = 1988
amount = 50000000

#동일 아저씨 방법
while year < 2016:                              # 2016년은 포함하면 안된다.
    amount = amount * (1 + INTEREST_RATE)
    year = year + 1

#계산
if amount > APT_PRICE:
    print("%d원 차이로 동일 아저씨의 말씀이 맞습니다" % (amount - APT_PRICE))
else:
    print("%d원 차이로 미란 아주머니의 말씀이 맞습니다" % (APT_PRICE - amount))

# 피보나치 수열
print()
previous = 0
current = 1
i = 0
while i < 20:
    print(current)
    temp = previous
    previous = current
    current = current + temp
    i = i + 1

# 구구단
print()
first = 1
while first <= 9:
    second = 1
    while second <= 9:
        print("%d * %d = %d" % (first, second, first * second))
        second = second + 1
    first = first + 1


# 꿀팁
# Break 문
print()
i = 100
while True:
    if i % 23 == 0:
        break       # i가 23의 배수이면 while을 끝냄
    i = i + 1
print(i)

# Continue 문
print ()
i = 0
while i < 15:
    i = i + 1
    if i % 2 == 0:
        continue    # 짝수이면 무시하고 조건으로 돌려보냄
    print(i)