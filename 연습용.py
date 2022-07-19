def func():
    flag = True

    while flag:
         SSN = input("주민번호를 입력하세요 : ")
    if  len(SSN) == 14 and SSN[6] == '-':
         SSN = SSN.split('-')[0] + SSN.split('-')[1]
    elif len(SSN) == 13:
        pass
    
    else:
        print("잘못된 주민번호입니다.")
        continue    

    print('result = ', SSN[:6] + ('*' * 7))
    flag = false


func()