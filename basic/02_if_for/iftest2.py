# 숫자를 입력받아서 짝수/홀수 판별

num = input("숫자 입력 > ")

if num.isdecimal(): #숫자인지 판별하는 구문
    num=int(num)
    if num%2 == 0 :
        print("짝수")
    else :
        print("홀수")
else :
    print("숫자를 입력하세요")