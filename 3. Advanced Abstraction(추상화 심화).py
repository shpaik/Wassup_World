##추상화 심화
# Return
# 1. return문 뒤에 오는 값으로 대체
print("Return - 1")
def f(x):
    return x + 1
print(f(2))  # = print(3), f(2)가 3으로 대체된다

# 2. 현재 함수를 멈추고 함수가 호출된 지점으로 돌아감
print("\nReturn - 2")
def f(x):
    print("f start")
    return(x + 1)
    print("f end")  #Dead Code: 실행되지 않는 코드. return이 나오고 print(f(2))는 끝남.
def g(x):
    print("g start")
    return x * x - 1
    print("g end")
print(f(2))    # 11번으로 f함수를 찾은후 "f start"를 출력한다. 그다음 내려가 return이 나왔으니 f(2)는 3으로 대체(1). 그리고 19로 넘어감 (2).
print(g(3))
print(f(2) * g(3))

# Return Vs. Print
print("\nReturn Vs. Print")
def print_square(x):
    print( x * x)
def get_square(x):
    return x * x
print_square(3)
print("--")
get_square(3)  # 그냥 get_squre(3)가 9랑 똑같음. 명령문이 없으니 아무것도 ㄴㄴ
print("--")
print(get_square(3))  # print(9)로 바뀜.
print("--")
print(print_square(3))  #print_square(3) 를 먼저 인식함 -> 9먼저 뽑음. 그리고 print(print_square(3))를 인식해서 None

# Example
print("\nExample")
def secret_number():
    print("나를 여는 비밀 번호는")
    return 486
secret_number()
print("--")
print(secret_number())

# Global & Local 변수
print("\nGlobal & Local 변수")
def x_is_one():
    x = 1   # Local: 한 부분에서만 유효한 변수 (함수에서 defined)
x = 5       # Global: 모든 부분에서 유효한 변수
x_is_one()
print(x)

def x_is_one():
    global x
    x = 1
x = 5       # x 는 5로 지정됨
x_is_one()  # globalizer x, x는 1로 새롭게 defined
print(x)

print( int("5") + int(2.0))

# 상수 (Constant)
#  바뀌지 않는 Global Variable.
#  대문자로 사용
#  바꿔도 되지만 안바꾸는게 철칙
# 한줄에 80자 오바 ㄴㄴ

# 짝수 or 홀수
print()
def is_evenly_divisible(number):
    return ((number) % 2) == 0

print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))