import re

custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong@gmail.com', 'birth':2000},
            {'name': '고길동', 'gender': 'M', 'email': 'gildong@gmail.com', 'birth':2011},
            {'name': '박나리', 'gender': 'F', 'email': 'nari@gmail.com', 'birth':2010},
            {'name': '김철수', 'gender': 'M', 'email': 'stealwater@gmail.com', 'birth':1988},]
page=3



while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()
  

    if choice=="I":        
        print("고객 정보 입력")
        customer = {'name':'', 'gender':'', "email":'', "birth":''}
        customer['name'] = input("이름 >> ")

        # M 혹은 F로만 입력 받는다. 소문자의 경우 upper를 활용하여 대문자로 만든다.
        while True :
            gender = input("성별(M/F) >> ")
            gender = gender.upper()
            if gender == 'M' or gender == 'F' :
                customer['gender'] = gender
                break
            else :
                print("M 혹은 F를 입력해주세요.")
                
        while True :
            
            email = input("이메일 >> ")
            same = 0
            # 중복 이메일 확인
            for i in custlist:
                if i['email'] == str(email):
                    print('중복되는 이메일이 있습니다.')
                    same += 1
                    break
                

            # 정규표현식과 대조                
            if same == 0 :    
                p = re.compile('[a-z0-9]{4,}@[a-z]{2,}[.][a-z]{2,5}')
                result = p.match(email)
                if result == None :
                    print("이메일 주소를 확인해 주세요.")
                else :
                    customer[email] = str(email)
                    break

        while True:
            customer['birth'] = input("출생년도 >>")
            if len(customer['birth']) == 4 and customer['birth']:
                customer['birth'] = int(customer['birth'])
                break

        custlist.append(customer)
        page += 1

    elif choice=="C":
        print("현재 고객 정보 조회")
        if page >= 0 :
            print("현재 페이지는 {}쪽 입니다.".format(page+1))
            print(custlist[page])
        else :
            print("입력된 정보가 없습니다.")

    elif choice == 'P':
        print("이전 고객 정보 조회")
        if page <= 0 :
            print("첫번째 페이지 입니다. 이전페이지로 이동할 수 없습니다.")
            print(custlist[-1])
        else :
            page -=1
            print("현재 페이지는 {}쪽 입니다.".format(page+1))
            print(custlist[page])

    elif choice == 'N':
        print("다음 고객 정보 조회")
        if page >= len(custlist)-1:
            print('현재 페이지는 {}쪽, 마지막 페이지 입니다. 다음 페이지로 이동할 수 없습니다.'.format(page+1))
            print(custlist[page])
        else :
            page += 1
            print("현재 페이지는 {}쪽 입니다.".format(page+1))
            print(custlist[page])

    elif choice=='D':
        print("고객 정보 삭제")

        for i in custlist:
            print(i['name'], ':', i['email'], end = "\n")
        print()

        delete = input("삭제할 고객의 이메일을 입력해 주세요.")
        delok = 0
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == delete:
                print('{} 고객님의 정보가 삭제되었습니다.}'.format(custlist[i]['name']))
                del custlist[i]
                delok = 1

            if delok == 1:
                break
        if delok == 0 :
            print('등록되지 않은 이메일입니다.')    
            

    elif choice=="U": 
        print("고객 정보 수정")
        for i in custlist:
            print(i['name'], ':', i['email'], end = "\n")
        print()
        while True:
            choice1 = input("수정할 고객의 이메일을 입력해 주세요.")
            idx=-1
            for i in range(0,len(custlist)):
                if custlist[i]['email'] == choice1:
                    idx=1
            if idx==-1:
                print('등록되지 않은 이메일입니다.')
                break

            choice2=input('''
            다음 중 수정하실 정보를 선택해 주세요.
                    name, gender, birth
            (수정할 정보가 없을 시, 'exit'입력)
            ''')
            if choice2 in ('name','gender','birth'):
                custlist[idx][choice2]=input("변경하실 {} : ".format(choice2))
                for i in custlist:
                    print(i['name'],":",i['email'])
                print()
                break
            elif choice2 == 'exit':
                break
    elif choice=="Q":
        print("프로그램 종료")
        break