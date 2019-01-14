#FormConversion
#number -> number
print(int(3.8))
print(float(3))

#String -> Number
print(int("2") + int("5"))
print(float("1.1") + float("2.5"))

#Number -> string
print(str(2)+str(5))
print("제 나이는"+ str(7) +"살입니다.")


print(int(float("3.0")))
print(float(int(42/5)))

#날짜
year = 2018
month = 1
day = 16
day_of_week = "일"
print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일 " + day_of_week + "요일입니다.")

#String Formatting(문자열 포매팅)
## %d 정수
## %f 소수
## %s 문자열
print("오늘은 %d년 %d월 %d일 %s요일입니다." % (2000, month, day, day_of_week))  #앞에=틀
print("오늘은 %d년 %d월 %d일 %s요일입니다." % (year, month, day+1, "월"))
#소수를 틀에 넣고 싶을때
print(1.0 / 3)
print("1 나누기 3은 %.4f" % (1.0 / 3))  #f = floating, .4 = 원하는 decimal point

#Boolean
#Boolean Algebra: 진릿값. (True/False) (And, or not)
#명제: 참 또는 거짓이 확실한 문장
# And: 둘다 참이여야 참.
print()
print(True and True)
print(False and True)
print(False and False)
# Or: 둘중의 하나만 참이면 참.
print(True or True)
print(False or True)
print(False or False)
# Not: T->F
print()
print(not True)
print(not False)
print()
print(2 == 2) #같다
print(2 != 2) #다르다
print(2 > 1 and "Hello" == "Hello")
print(not not True)

#Type 함수: 자료형 확인하기!
print()
print("type함수")
print(type(1))
print(type(1.0))
print(type("1"))

print()
print("퀴즈")
print(int(str(1) + str(2)))

#Floor Division & Round & Newline
print()
print("Floor Division & Round & Newline")
print(7/4)
print(7//4)
print(7.0//4)
print()
print(round(1.412,1))
print()
print("이건\n줄바꿈\nㅋ")
