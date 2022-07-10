class Donkey:
    def __init__(self,age:int,weight:float):
        self.age = age
        self.weight = weight

    def sound(self):
        print(f'Donkey makes eeyore sound')

    def show_info(self):
        print(f'Age: {self.age}')
        print(f'weight: {self.weight}')

if __name__ == "__main__":
    donkey = Donkey(2,100)
    print(donkey.show_info())