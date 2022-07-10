from horse import Horse
from donkey import Donkey

class Mule(Horse,Donkey):
    def __init__(self, name: str, color: str, age:int , weight:float):
        super().__init__(name, color)
        super(Horse, self).__init__(age, weight)

    def run(self):
        print(f'{self.name} is running')
    
    def show_info(self):
        print(f'Name: {self.name}')
        print(f'Color: {self.color}')
        print(f'Max Height: {Horse.max_height} cm')
        print(f'Age: {self.age}')
        print(f'weight: {self.weight}')

if __name__ == "__main__":
    mule1 = Mule('Mumu','Blue-eyed cream',3,200)
    mule2 = Mule('Meme','Palomino',1,120.7)
    print(f'===== {mule1.name} =====')
    print(mule1.show_info())
    print(f'===== {mule2.name} =====')
    mule2.sound()
    print(mule2.show_info())