from country_abstract import Country

class Europe(Country):
    def __init__(self, name, pop) -> None:
        super().__init__(name, pop)
        self.__location = None
        self.__capital = ""

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self,value):
        self.__location = value

    @property
    def capital(self):
        return self.__capital
    @capital.setter
    def capital(self,value):
        self.__capital = value
    
    def show_detail(self):
        super().show_detail()
        print("===== Europe =====")
        print(f'country: {self.name}')
        print(f'capital: {self.capital}')
        print(f'poppulation: {self.population:,}')
        print(f'location: {self.location}')

class Asia(Country):
    def __init__(self, name, pop) -> None:
        super().__init__(name, pop)
        self.__gdp = 0
        
    @property
    def gdp(self):
        return self.__gdp
    @gdp.setter
    def gdp(self,value):
        self.__gdp = value
        
    def show_detail(self):
        super().show_detail()
        print("===== Europe =====")
        print(f'country: {self.name}')
        print(f'poppulation: {self.population:,}')
        print(f'gdp: {self.gdp} billion USD')