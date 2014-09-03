class Wheel():
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

class Frame():
    def __init__(self, composition, weight, cost):
        self.composition = composition
        self.weight = weight
        self.cost = cost

class Bicycle_Model():
    def __init__(self, name, manufacturer, wheel, frame):
        self.name = name
        self.manufacturer = manufacturer # this is a string
        self.weight = 2 * wheel.weight + frame.weight
        self.cost = 2 * wheel.cost + frame.cost

class Bicycle_Manufacturer():
    def __init__(self, name, models, percentage):
        self.name = name
        self.models = models # this will be a list of bike model objects
        self.percentage = percentage

class Bike_Shop():
    def __init__(self, name, manufacturers, margin):
        self.name = name
        self.margin = margin
        self.profit = 0
        self.manufacturers = manufacturers
        # manufacturers is a list of manufacturer objects
        self.inventory = dict()
        self.costs = {}
        for manufacturer in manufacturers:
            for model in manufacturer.models:
                self.inventory[model.name] = 0
                self.costs[model.name] = (1+manufacturer.percentage)*model.cost

    def buy_model(self, model, amount=1):
        self.inventory[model.name] += amount

    def sell_model(self, model, amount=1):
        self.inventory[model.name] -= amount
        self.profit += self.margin * self.costs[model.name]

class Customer():
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        self.bicycle = []

    def buy_bicycle(self, bike, cost):
        if cost > self.funds:
            print "Sorry, you don't have enough money."
        else:
            self.funds -= cost
            self.bicycle.append(bike)
