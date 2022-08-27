from tkinter.messagebox import showinfo


class Car:
    def __init__(self, name, gradyear, prodycer, engine_capacity, color, price):
        self.__name = name
        self.__gradyear = gradyear
        self.__prodycer = prodycer
        self.__engine_capacity = engine_capacity
        self.__color = color
        self.__price = price

    def show_info(self):
        print(f"Автомобіль {self.__name} виробництва {self.__prodycer}, {self.__gradyear} года випуску, об'ємом "
              f"двигуна {self.__engine_capacity}л, {self.__color} кольору коштує {self.__price}$")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def gradyear(self):
        return self.__gradyear

    @gradyear.setter
    def gradyear(self, gradyear):
        self.__gradyear = gradyear

    @property
    def prodycer(self):
        return self.__prodycer

    @prodycer.setter
    def prodycer(self, prodycer):
        self.__prodycer = prodycer

    @property
    def engine_capacity(self):
        return self.__engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, engine_capacity):
        self.__engine_capacity = engine_capacity

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
mercedes = Car (
    name="Mercedes-Benz GLE-class c167",
    gradyear=2021,
    prodycer="Mercedes-Benz Group",
    engine_capacity=2.9,
    color="white",
    price=4_000_000
)

lexus = Car (
    name="Lexus NX 200 D-CVT Urban 2022 (1J7)",
    gradyear=2022,
    prodycer="Toyota Motors",
    engine_capacity=2.0,
    color="tabaco",
    price=2_000_000
)

bentley = Car (
    name="Bentley Continental GT V8 4.0i AT AWD 2021",
    gradyear=2021,
    prodycer="Bentley Motors LTD",
    engine_capacity=4.0,
    color="black",
    price=12_000_000
)

bentley.show_info()
lexus.show_info()
mercedes.show_info()