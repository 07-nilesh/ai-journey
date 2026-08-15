class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand  # __brand means it is now private 
        self.model=model    # it cannot be acceseed by object we have to make function for it.
        Car.total_car+=1
    def get_brand(self):
        return self.__brand+ "!"

    def full_name(self):
        return f"{self.__brand},{self.model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    @staticmethod
    def general():
        return " cars are means of transport"
    
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    
    def fuel_type(self):
        return " electricity"
my_tesla=ElectricCar("tesla","Model s","85kwh")
print(my_tesla.full_name())
print(my_tesla.fuel_type())
my_car=Car("toyota","corolla")
print(my_car.full_name())
print(my_car.fuel_type())
print(Car.total_car)
print(Car.general())
print(my_car.general())
print(isinstance(my_car,Car))

class Battery:
    def battery_info(self):
        return "this is battery"
    
class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCar2(Battery,Engine,Car):
    pass
my_tata=ElectricCar2("Tata","nexon")
print(my_tata.engine_info())
    