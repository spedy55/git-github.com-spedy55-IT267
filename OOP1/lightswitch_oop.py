
class Light_Switch():
    def __init__(self) -> None:
        self.switch_status = False
    def turnon(self):
        self.switch_status = True
    def turnoff(self):
        self.switch_status = False
    def show(self):
        print(f"Status = {self.switch_status}")

Switch_object = Light_Switch()

Switch_object.show()
Switch_object.turnon()
Switch_object.show()
Switch_object.turnoff()
Switch_object.show()
Switch_object.turnoff()
Switch_object.show()