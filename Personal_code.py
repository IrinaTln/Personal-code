ik=""
kuu=""
paev=""
aasta=""
print("Анализ личного кода".center(50,"*"))
while len(ik)!=11 or ik.isdigit()!=True or int(list(ik)[0]) not in [1,2,3,4,5,6] or int(list(ik)[3]+list(ik)[4])<0 or int(list(ik)[3]+list(ik)[4])>13 or jaak!=int(list(ik)[10]):
    try:
        ik=input("Введите личный код: ")
        ik_list=list(ik)
        if int(ik_list[0]) not in [1,2,3,4,5,6]:
            print("Первая цифра личного кода указана неверно")
        
        kuu=ik_list[3]+ik_list[4]
        kuu=int(kuu) #если это не указать, то все даты до 10 месяца будут не существующими
        paev=int(ik_list[5]+ik_list[6])
        if int(ik_list[0])==1 or int(ik_list[0])==2:
            aasta=int("18"+ik_list[1]+ik_list[2])
        elif int(ik_list[0])==3 or int(ik_list[0])==4:
            aasta=int("19"+ik_list[1]+ik_list[2])
        elif int(ik_list[0])==5 or int(ik_list[0])==6:
            aasta=int("20"+ik_list[1]+ik_list[2])
        if kuu in [1,3,5,7,8,10,12] and paev>0 and paev<32:
            print(ik_list[5],ik_list[6]," - ваша дата рождения.")
        elif (kuu in [4,6,9,11] and paev>0 and paev<31) or( kuu==2 and paev>0 and paev<29):
            print(ik_list[5],ik_list[6]," - ваша дата рождения.")
        elif aasta % 4==0 and kuu ==2 and paev>0 and paev<30:
            print(ik_list[5],ik_list[6]," - ваша дата рождения.")
        else:
            print(ik_list[5],ik_list[6]," - не существующая дата!")
            
        kuu=int(ik_list[3]+ik_list[4]) #это склеивание цифр из списка. не сложение!
        if kuu>0 and kuu<13:
            print(ik_list[3],ik_list[4], " - ваш месяц рождения.")
        else:
            print(ik_list[3],ik_list[4], " - не существующий месяц!")
            
        aasta=int(ik_list[1]+ik_list[2]) #скливаем цифры года рождения
        if int(ik_list[0])==1 or int(ik_list[0])==2:
            print("18",ik_list[1], ik_list[2]," - ваш год рождения")
        elif int(ik_list[0])==3 or int(ik_list[0])==4:
            print("19",ik_list[1],ik_list[2]," - ваш год рождения.")
        elif int(ik_list[0])==5 or int(ik_list[0])==6:
            print("20",ik_list[1],ik_list[2]," - ваш год рождения.")
        summa=0
        for i in range(1,11):
            if i<10:
                summa+=i*int(ik_list[i-1])
            else:
                summa+=(i-9)*int(ik_list[i-1])
        print("Сумма: ", summa)
        jaak=summa//11
        if jaak==10: 
            summa=0
            for i in range(3,13):
                if i<=9:
                    summa+=i*int(ik_list[i-1])
                else:
                    summa+=(i-9)*int(ik_list[i-1])
            jaak=summa//11
            print(jaak)
        jaak=summa-jaak*11
        if jaak==10:
            jaak=0
        print("Контрольная сумма равна: ", jaak)
        if jaak==int(ik_list[10]):
            print("Личный код верен.")
        else: 
            print("Не верный личный код.")
    except ValueError:
        print("Вы указали неверные данные.")