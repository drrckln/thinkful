class Animal(object):
    def __init__(self, name, legs, color):
        self.name = name
        self.legs = legs
        self.color = color

    def __repr__(self):
        return "I am a {} with {} legs and my color is {}".format(self.name, self.legs, self.color)

lion = Animal("lion", 4, "yellow")

print lion
