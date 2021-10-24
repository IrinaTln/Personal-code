ik=""
kuu=""
paev=""
aasta=""
sunnitusmaja=""
sugu=""
print("Анализ личного кода".center(50,"*"))
while True:
    try:
        ik=input("Введите личный код: ")
        if len(ik)!=11:
            print("Вы указали неверные данные")
            continue
        ik_list=list(ik)
          
        kuu=ik_list[3]+ik_list[4]
        kuu=int(kuu) #если это не указать, то все даты до 10 месяца будут не существующими
        sunnitusmaja=ik_list[8]+ik_list[9]+ik_list[10]
        sunnitusmaja=int(sunnitusmaja)

        sugu=ik_list[0] #вывод пола владельца личного кода
        sugu=int(sugu)
        if sugu==1 or sugu==3 or sugu==5:
            print("Анализируемый личный код принадлежит мужчине.")
        elif sugu==2 or sugu==4 or sugu==6:
            print("Анализируемый личный код принадлежит женщине.")

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

        sunnitusmaja=int(ik_list[7]+ik_list[8]+ik_list[9]) #определяем место рождения
        if sunnitusmaja==1 or sunnitusmaja<=10:
            print("Вы родились в родильном доме Куресааре.")
        elif sunnitusmaja==11 or sunnitusmaja<=19:
            print("Вы родились в клинике Тартуского университета.")
        elif sunnitusmaja==21 or sunnitusmaja<=220:
            print("Вы родились в одном из родильных домов Таллинна, Хийумаа, Кейла, Рапла или же Локса.")
        elif sunnitusmaja==221 or sunnitusmaja<=270:
            print("Вы родились в одном из родильных домов Ида-Вирумаа, Кохтла-Ярве или Йыхви.")
        elif sunnitusmaja==271 or sunnitusmaja<=370:
            print("Вы родились в Тарту или Йыгева.")
        elif sunnitusmaja==371 or sunnitusmaja<=420:
            print("Вы родились в Нарве.")
        elif sunnitusmaja==421 or sunnitusmaja<=470:
            print("Вы родлись в Пярну.")
        elif sunnitusmaja==471 or sunnitusmaja<=490:
            print("Вы родились в Таллинне или в Хаапсалу.")
        elif sunnitusmaja==490 or sunnitusmaja<=520:
             print("Вы родились в Пайде.")
        elif sunnitusmaja==521 or sunnitusmaja<=570:
            print("Вы родились в Раквере или в Тапа.")
        elif sunnitusmaja==571 or sunnitusmaja<=600:
            print("Вы родились в Валга.")
        elif sunnitusmaja==601 or sunnitusmaja<=650:
            print("Вы родились в Вильянди.")
        elif sunnitusmaja==651 or sunnitusmaja<=700:
            print("Вы родились в Выру или Пыльва.")

        summa=0
        for i in range(1,11):
            if i<10:
                summa+=i*int(ik_list[i-1])
            else:
                summa+=(i-9)*int(ik_list[i-1])
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