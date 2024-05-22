"""Создайте класс "Автомобиль", который содержит информацию о марке, модели и
годе выпуска. Создайте класс "Грузовик", который наследуется от класса
"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
информацию о количестве пассажиров."""



class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Truck(Car):
    def __init__(self, brand, model, year, capacity):
        super().__init__(brand, model, year)
        self.capacity = capacity

class PassengerCar(Car):
    def __init__(self, brand, model, year, passengers):
        super().__init__(brand, model, year)
        self.passengers = passengers


truck1 = Truck('Volvo', 'VNL', 2021, 20000)
print(truck1.brand, truck1.model, truck1.year, truck1.capacity)

car1 = PassengerCar('Toyota', 'Camry', 2019, 5)
print(car1.brand, car1.model, car1.year, car1.passengers)