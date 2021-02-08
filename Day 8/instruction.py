# Object to hold all three values of an instruction
class Instruction():
    def __init__(self,action,value):
        self.action = action
        self.value = value
        self.seen = False
    
    def display(self):
        print(self.action, self.value, self.seen)