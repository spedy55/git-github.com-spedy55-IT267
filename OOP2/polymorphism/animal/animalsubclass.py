from animal import Animal

class Dog(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    
    def info(self):
        super().info()
        Animal.info(self) #ได้ข้อความ animal information
        print(f'I am a dog.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} years old')

    def make_sound(self):
        super().make_sound()
        Animal.make_sound(self)
        print(f'Hey! i make Woof!! Woof!! sound')

class Cat(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    
    def info(self):
        super().info()
        Animal.info(self) #ได้ข้อความ animal information
        print(f'I am a Cat.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} years old')

    def make_sound(self):
        super().make_sound()
        Animal.make_sound(self)
        print(f'Hey! i make Meow!! Meow!! sound')

class Cow(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    
    def info(self):
        super().info()
        Animal.info(self) #ได้ข้อความ animal information
        print(f'I am a Cow.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} years old')

    def make_sound(self):
        super().make_sound()
        Animal.make_sound(self)
        print(f'Hey! i make Mooo!! Mooo!! sound')