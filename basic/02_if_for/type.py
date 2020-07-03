import random
import time

word = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

correct=0
n=1
input("타자 게임 \n    << PRESS ENTER TO START >>")
start=time.time()
while n<=10 :
    i = random.randint(3, 10)
    result = ''
    for j in range(0, i):
        quiz = random.choice(word)
        result += str(quiz)
    print("\n")
    while (n != correct) :
        print(result)
        answer = input()
        if answer == result:
            print("정답입니다!")
            correct+=1
            n += 1
            break
        else:
            print("잘못 입력하였습니다")

end= time.time()

et= end-start
print("경과시간 {:.0f}초".format(et))