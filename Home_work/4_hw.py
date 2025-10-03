class House():
    """описание дома"""
    def __init__(self, street, number):
        """свойство дома"""
        self.street = street
        self.number = number
    
    def build(self):
        """Строит дом"""
        print("Дом на улице " + self.street + " под номером " + str(self.number) + " построен.")

House1 = House("Московская", 20)
House2 = House("Московская", 21)      

House1.build()
House2.build()
print("==================================================================================================")

#-------------------------------------------------------------------------------------------------------

class Rectangle():
    def __init__(self, a=int(input()), h=int(input())): #a-ширина, h-высота
        self.a = a
        self.h = h
        

    def perimeter(self):
        print('Периметр прямоугольника с шириной ' + str(self.a) + ' и высотой ' + str(self.h) + ' равен ', (self.a+self.h)*2 )
    def area(self):    
        print('Площадь прямоугольника с шириной ' + str(self.a) + ' и высотой ' + str(self.h) + ' равен ', self.a*self.h)

Result = Rectangle()

Result.perimeter()
Result.area()
print("==================================================================================================")

#-------------------------------------------------------------------------------------------------------

class Math():
    def __init__(self, a=int(input()), b=int(input())):
        self.a = a
        self.b = b 

    def addition(self):
        print('Сложение равно', self.a + self.b)
    
    def multiplication(self):
        print('Умножение равно' ,self.a * self.b)
    
    def division(self):
        print('Деление равно' ,self.a / self.b)
    
    def subtraction(self):
        print('Вычитание равно', self.a - self.b)
    
Result = Math()

Result.addition()
Result.multiplication()
Result.division()
Result.subtraction() 
print("==================================================================================================")

#-------------------------------------------------------------------------------------------------------

class Button:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = "" 

    def click(self):
        return f"Клик по кнопке {self.text}"

text_box_button = Button("Text Box")
check_box_button = Button("Check Box")
radio_button_button = Button("Radio Button")
web_tables_button = Button("Web Tables")
buttons_button = Button("Buttons")
links_button = Button("Links")
broken_links_images_button = Button("Broken Links - Images")
upload_download_button = Button("Upload and Download")
dynamic_properties_button = Button("Dynamic Properties")

# Список всех кнопок
all_buttons = [
    text_box_button,
    check_box_button,
    radio_button_button,
    web_tables_button,
    buttons_button,
    links_button,
    broken_links_images_button,
    upload_download_button,
    dynamic_properties_button
]
print("Текст для каждой кнопки:")
for button in all_buttons:
    print(f"- {button.text}")

print("\nВызов метода 'Клик' для каждой кнопки:")
for button in all_buttons:
    print(button.click())