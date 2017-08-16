class Ninja:

    def __init__(self,name,colour):
        self.name = name
        self.colour = colour

    def introduce(self):
        print('I am ' , self.name)
        print('I am ' ,self.colour)

lloyd=Ninja('lloyd','green')

kai=Ninja('kai','red')

lloyd.introduce()
kai.introduce()
