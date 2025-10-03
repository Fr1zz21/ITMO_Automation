def function_1():
    a=int(input())
    b=int(input())
    if a>b:
        print(a)
    elif b>a:
        print(b)
    else: 
        print("Они равны")
function_1()

#---------------------------------------------------------------------------------------------------------

def function_2():
    a=int(input())
    b=int(input())
    if a-b == 135 or b-a == 135:
        print('YES')
    else:
        print("NO")
function_2()

#---------------------------------------------------------------------------------------------------------

def function_3():
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
function_3()

#---------------------------------------------------------------------------------------------------------

def function_4():
    a=int(input())
    b=int(input())
    c=int(input())
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")
function_4()
#---------------------------------------------------------------------------------------------------------

def function_5():
    mounth=29
    year=mounth*12
    a=int(input())
    b=int(input())
    print(b*29+year*a)
function_5()







