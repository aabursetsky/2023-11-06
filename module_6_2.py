class Vehicle:
    __COLOR_VARIANTS = ['black', 'grey', 'white', 'red', 'yellow', 'green']

    # def __init__(self, owner, model, engine_power, color):
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return f'{self.__engine_power}'

    def get_color(self):
        return self.__color

    def print_info(self):
        print("Модель:", self.get_model())
        print("Мощность:", self.get_horsepower())
        print("Цвет:", self.get_color())
        print(f'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.capitalize()     # Первая заглавная остальные строчные
        else:                                         # Если меняется значение
            print(f'Нельзя сменить цвет на {new_color}')


# Наследник класса Vehicle
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['black', 'grey', 'white', 'red', 'yellow', 'green']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
# Проверяем что поменялось
vehicle1.print_info()
vehicle1.set_color('YelloW')
# Проверяем что поменялось
vehicle1.print_info()
vehicle1.set_color('BLACK')
# Проверяем что поменялось
vehicle1.print_info()
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()

'''
Модель: Toyota Mark II
Мощность: 500
Цвет: blue
Владелец: Fedos

Нельзя сменить цвет на Pink
Модель: Toyota Mark II
Мощность: 500
Цвет: blue
Владелец: Fedos

Модель: Toyota Mark II
Мощность: 500
Цвет: Yellow
Владелец: Fedos

Модель: Toyota Mark II
Мощность: 500
Цвет: Black
Владелец: Fedos

Модель: Toyota Mark II
Мощность: 500
Цвет: Black
Владелец: Vasyok
'''
