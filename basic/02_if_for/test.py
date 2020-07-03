import random
import time

# correct=0
# wrong=0
# for i in range(0,10):
#     a = random.randint(1,50)
#     b = random.randint(1,50)
#     answer = int(input("{} + {} = ? \n".format(a,b)))
#     if answer == (a+b):
#         print("정답입니다!")
#         correct+=1
#     else:
#         print("오답입니다...")
#         wrong+=1

# print("10문제 중 {}개 정답 {}개 오답".format(correct,wrong))




# print (random.randint(1,50))
# oprator=["+","-","/","*"]
# print(random.choice(oprator))

# a="23*34"
# print(a)
# print(eval(a))




correct=0
wrong=0
oprator=["+","-","*"]
input("사칙연산 QUIZ! \nPRESS ENTER >>")
start=time.time()
for i in range(0,10):
    a = random.randint(1,50)
    b = random.randint(1,50)
    oper = random.choice(oprator)
    quiz = str(a) + " " + oper + " " + str(b)
    answer = int(input("{} = ? \n".format(quiz)))
    if answer == eval(str(a) + oper + str(b)):
        print("정답입니다!")
        correct+=1
    else:
        print("오답입니다... 정답은 {}입니다.".format(eval(quiz)))
        wrong+=1
end= time.time()

et= end-start
print("경과시간 {}초\n10문제 중 {}개 정답 {}개 오답".format(et,correct,wrong))