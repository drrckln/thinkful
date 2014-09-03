import models

wheel1 = models.Wheel("wheel1", 10, 30)
wheel2 = models.Wheel("wheel2", 8, 25)
wheel3 = models.Wheel("wheel3", 6, 20)

frame1 = models.Frame("frame1", 15, 40)
frame2 = models.Frame("frame2", 10, 50)
frame3 = models.Frame("frame3", 13, 45)

bike1 = models.Bicycle_Model("bike1", "manufacturer1", wheel1, frame1)
bike2 = models.Bicycle_Model("bike2", "manufacturer1", wheel2, frame2)
bike3 = models.Bicycle_Model("bike3", "manufacturer1", wheel3, frame3)
bike4 = models.Bicycle_Model("bike4", "manufacturer2", wheel1, frame1)
bike5 = models.Bicycle_Model("bike5", "manufacturer2", wheel2, frame2)
bike6 = models.Bicycle_Model("bike6", "manufacturer2", wheel3, frame3)

manufacturer1 = models.Bicycle_Manufacturer("manufacturer1", [bike1, bike2, bike3], 0.25)
manufacturer2 = models.Bicycle_Manufacturer("manufacturer2", [bike4, bike5, bike6], 0.20)

bike_shop_1 = models.Bike_Shop("bike shop 1", [manufacturer1, manufacturer2], 0.20)
bike_shop_2 = models.Bike_Shop("bike shop 2", [manufacturer1, manufacturer2], 0.25)

alex = models.Customer("Alex", 200)
ben = models.Customer("Ben", 500)
fred = models.Customer("Fred", 1000)

for manufacturer in bike_shop_1.manufacturers:
    for model in manufacturer.models:
        print model.name, model.weight

