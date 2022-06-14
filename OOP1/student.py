class Student:
    def __init__(self,id:str,name:str,major:str):
        self.id = id
        self.name = name
        self.major = major

    def display_detail(self):
        print(f"ID : {self.id}\nName : {self.name}\nMajor : {self.major}")

    def __del__(self):
        print(f"Object was destroy")

if __name__ == "__main__":
    jess = Student(111,"Jessica","IT\n")
    jess.display_detail()
    john = Student(112,"John","MKT\n")
    john.display_detail()