# Создайте класс "Автомобиль" с атрибутами "марка" и "год выпуска". Создайте объекты, представляющие разные автомобили, и выведите информацию о них


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_info(self):
        return f"Марка: {self.brand}, Год выпуска: {self.year}"


class ElectricCar(Car):
    def __init__(self, brand, year, battery_capacity):
        super().__init__(brand, year)
        self.battery_capacity = battery_capacity

    def get_info(self):
        return f"Марка: {self.brand}, Год выпуска: {self.year}, Емкость аккумулятора: {self.battery_capacity}"


class SportsCar(Car):
    def __init__(self, brand, year, max_speed):
        super().__init__(brand, year)
        self.max_speed = max_speed

    def get_info(self):
        return f"Марка: {self.brand}, Год выпуска: {self.year}, Максимальная скорость: {self.max_speed}"


class Buyer:
    def buy_car(self, car):
        try:
            if isinstance(car, ElectricCar):
                print("Покупка электрокара:")
                print(car.get_info())
            elif isinstance(car, SportsCar):
                print("Покупка спорткара:")
                print(car.get_info())
            else:
                print("Покупка автомобиля:")
                print(car.get_info())
        except AttributeError:
            print("Ошибка! Неверный объект автомобиля.")


# Создаем объекты разных автомобилей
car1 = Car("Toyota", 2010)
electric_car1 = ElectricCar("Tesla", 2022, 75)
sports_car1 = SportsCar("Ferrari", 2018, 320)

# Создаем объект покупателя
buyer = Buyer()

# Демонстрируем покупку разных автомобилей
buyer.buy_car(car1)
buyer.buy_car(electric_car1)
buyer.buy_car(sports_car1)
