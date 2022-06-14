#def = method / class อยู่ใน class / instance อยู่ใน method / object เรียกใช้ method

class Person:
    country = "Thailand"
    def __init__(self,name,gender,profession,hour):
        self.name = name
        self.gender = gender
        self.profession = profession
        self.hour = hour

    def work(self):
        print(f'{self.name} is working as a {self.profession}')

    def study(self):
        print(f'{self.name} studies for a {self.hour} hour(s)\n')
    
    def show(self):
        print(f'Name : {self.name}\nGender : {self.gender}\nProfession : {self.profession}\nStudy : {self.hour}')
        
    def __del__(self):
        print(f'Object was destroy')

jessa = Person("Jessa","Female","Software Engineer","10")
jessa.show()
jessa.work()
jessa.study()


jon = Person("Jon","Male","Doctor","15")
jon.show()
jon.work()
jon.study()

lisa = Person("lisa","Female","Korean Single","13")
lisa.work()

print(f"Class Variable : {Person.country}")
print(f"Instance Variable : {lisa.country}")

lisa.country = "Korea"
print(f"\nClass Variable : {Person.country}")
print(f"Instance Variable : {lisa.country}")
print(f"Instance Variable : {jon.country}")

Person.country = "England"
print(f"\nClass Variable : {Person.country}")
print(f"Instance Variable : {lisa.country}")
print(f"Instance Variable : {jon.country}")