#추상화
# 변수 (variable)
print("# 변수 (variable)")

x = 2 + 1
print(x)
x = x + 1
print(x)

speed = 10.438413361  #지정연산자 (Assignment Operator)  # 우사인 볼트의 평균속도
print(speed * 60)
print(speed * 120)

# 함수 (function)
print("\n#함수 (function)")
def hello(): #header
    print("Hello, World!")
    print("Welcome to my world!")
hello()


# 함수 (Function with Parameters)
print("\n#함수 (function w/ parameters)")

def Helloname(name):
    print("Hello, %s!" % (name))
    print("Welcome to my movie!")
Helloname("최은하")
def 더하기(a, b):
    print(a + b)
더하기(4, 2)

def print_full_name(first_name, last_name):
    print("%s, %s" % (last_name, first_name))
print_full_name("수민", "이")
print_full_name("은하", "최")

#거스름돈 계산기
def calculate_change(payment, cost):
    change = payment - cost
    #계산
    Fifty_K = int((change) / 50000)
    Ten_K =   int((change) % 50000) / 10000
    Five_K =  int((change) % 10000) / 5000
    One_K =   int((change) % 5000) / 1000

    #답
    print("50000원 지폐: %d장" % Fifty_K)
    print("10000원 지폐: %d장" % Ten_K)
    print("5000원 지폐: %d장" % Five_K)
    print("10000원 지폐: %d장" % One_K)

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

#Syntactic Sugar #간략하게 쓸 수 있는 문법
print("\n" + "Syntactic Sugar")
x = 2
x = x + 1
print(x)
x += 1
print(x)
x *= 2
print(x)

#Optional Parameters (Default Value)
print("\nOptional Parameters")
def myself(name, age = 24, nationality = "한국"):
    print("내 이름은 %s" % name)
    print("나이는 %d" % age)
    print("국적은 %s" % nationality)
myself("백승환")

