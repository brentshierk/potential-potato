class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed =breed
        print('dog intialized')
    
    def bark(self):
        print('Woof!')
    def sit(self):
        print(f"{self.name} sit's down")
    def rollOver(self):
        print(f"{self.name} rolls over")


