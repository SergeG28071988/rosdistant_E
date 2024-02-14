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

# Создаем еще несколько объектов автомобилей
car2 = Car("Ford", 2015)
electric_car2 = ElectricCar("Nissan", 2021, 60)
sports_car2 = SportsCar("Lamborghini", 2019, 350)

# Демонстрируем покупку разных автомобилей
buyer.buy_car(car2)
buyer.buy_car(electric_car2)
buyer.buy_car(sports_car2)

# Создаем еще несколько объектов автомобилей
car3 = Car("Toyota", 2018)
electric_car3 = ElectricCar("Tesla", 2020, 80)
sports_car3 = SportsCar("Ferrari", 2017, 320)

# Демонстрируем покупку разных автомобилей
buyer.buy_car(car3)
buyer.buy_car(electric_car3)
buyer.buy_car(sports_car3)

# Создаем еще несколько объектов автомобилей
car4 = Car("Honda", 2016)
electric_car4 = ElectricCar("Chevrolet", 2019, 70)
sports_car4 = SportsCar("Porsche", 2022, 360)

# Демонстрируем покупку разных автомобилей
buyer.buy_car(car4)
buyer.buy_car(electric_car4)
buyer.buy_car(sports_car4)

# Создаем еще несколько объектов автомобилей
car5 = Car("Mazda", 2017)
electric_car5 = ElectricCar("BMW", 2021, 90)
sports_car5 = SportsCar("Audi", 2019, 300)

# Демонстрируем покупку разных автомобилей
buyer.buy_car(car5)
buyer.buy_car(electric_car5)
buyer.buy_car(sports_car5)
