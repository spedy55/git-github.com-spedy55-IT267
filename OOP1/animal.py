class Animal:
    animal = "CAT"
    
    def new_animal(self,name:str,breed:str,colour:str,age:int):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.age = age

    def print_detial(self):
        print(f"-----------------")
        print(f"Name {self.name}")
        print(f"Animal {self.animal}")
        print(f"Breed {self.breed}")
        print(f"Colour {self.colour}")
        print(f"Age {self.age}")

if __name__ == "__main__":
    Animal.animal = "Fish"
    ula = Animal()
    ula.animal = "Dog"
    ula.new_animal("Ula","scottish","white",1)
    ula.print_detial()

    drac = Animal()
    drac.new_animal("Drac","Scottish","White",1)
    drac.print_detial()
    drac.breed = "Catfish"
    drac.print_detial()

    Animal.print_detial(ula)
    Animal.print_detial(drac)

    print(f'{Animal.__dict__}')
    
    print(f'{ula.__dict__}')

    peter = Animal()
    peter.new_animal("Peter","Parrot","green yellow red",2)
    peter.legs = 2
    print(f"{peter.__dict__}")