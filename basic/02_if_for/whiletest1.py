prompt = '''

--------------------
    커피 자판기
--------------------
 1. 커피 메뉴 추가
 2. 커피 메뉴 삭제
 3. 커피 자판기 시작
 4. 커피 메뉴 리스트
 5. 종료
--------------------
 메뉴 선택 >>> '''


menudic = {'coffee' : 2000}


while True :
    print(prompt)
    menu = input()
    if menu.isdecimal():
        menu= int(menu)
        if menu == 1:
            print("커피 메뉴 추가")
            name = input("메뉴 이름 > ")
            price = int(input("가격 > "))
            menudic[name] = price
            print(menudic)

        elif menu == 2:
            print("커피 메뉴 삭제")
            print(menudic)
            name = input("삭제할 메뉴를 입력해 주세요 >")
            menudic.pop(name)
            print(menudic)


        elif menu == 3:
            print("커피 자판기 시작")
            print(menudic)
            choiceMenu = input("메뉴를 선택해 주세요 > ")
            inputMoney = int(input("투입 금액을 입력해주세요 > "))
            if menudic.get(choiceMenu)== None:
                print("메뉴 없음")
            else :
                if menudic[choiceMenu] > inputMoney :
                    print("금액이 부족합니다")
                else :
                    print("{} 음료가 나옵니다.".format(choiceMenu))
                    print("남은 금액 {}를 받으세요".format(inputMoney - menudic[choiceMenu]))

        elif menu == 4:
            for k,v in menudic.items():
                print("{}    {:,}원 ".format(k,v))

        elif menu == 5:
            print("프로그램 종료")
            break

    else :
        print("숫자를 입력해주세요")

