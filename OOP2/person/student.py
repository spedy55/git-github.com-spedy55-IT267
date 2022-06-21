from person import Person

class Student(Person):
    def __init__(self, name, faculity, major , year) -> None:
        super().__init__(name)
        self.faculity = faculity
        self.major = major
        self.year = year

    def welcome(self):
        super().welcome()
        print(f'Welcome to {self.faculity} major {self.major} in {self.year}')