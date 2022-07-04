from vehicle_abstract import Vehicle
class Car(Vehicle):
    def __init__(self, brand, speed) -> None:
        super().__init__(brand, speed)
        self.__year = 0
        self.__maintenance = 0

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self,value):
        self.__year = value
        
    @property
    def maintenance(self):
        return self.__maintenance
    @maintenance.setter
    def maintenance(self,value):
        self.__maintenance = value

    def show_detail(self):
        super().show_detail()
        print(f'===== Car Detail =====')
        print(f'{self.brand} with speed {self.speed} km/hr')
        print(f'manufactered in {self.year} has')
        print(f'{self.gear} gear and {self.seat} seats')
    
    def show_maintenance(self):
        print(f'===== Car Mainternance =====')
        print(f'The Las maintenance in {self.maintenance}')

class Truck(Vehicle):
    pass

class Motocycle(Vehicle):
    pass