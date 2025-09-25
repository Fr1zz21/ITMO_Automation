def zad_1():
    a=int(input())
    b=int(input())
    if a>b:
        print(a)
    elif b>a:
        print(b)
    else: 
        print("Они равны")
zad_1()

#---------------------------------------------------------------------------------------------------------

def zad_2():
    a=int(input())
    b=int(input())
    if a-b == 135 or b-a == 135:
        print('YES')
    else:
        print("NO")
zad_2()

#---------------------------------------------------------------------------------------------------------

def zad_3():
    a=int(input())
    if a > 12 or a < 1:
        print("Ошибка")
    elif a == 1 or a == 2 or a == 12:
        print('Зима')
    elif a == 3 or a == 4 or a == 5:
        print("Весна")
    elif a == 6 or a == 7 or a == 8:
        print("Лето")
    elif a == 9 or a == 10 or a == 11:
        print("Осень")
zad_3()

#---------------------------------------------------------------------------------------------------------

def zad_4():
    a=int(input())
    b=int(input())
    c=int(input())
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")
zad_4()
#---------------------------------------------------------------------------------------------------------

def zad_5():
    mes=29
    god=mes*12
    a=int(input())
    b=int(input())
    print(b*29+god*a)
zad_5()







