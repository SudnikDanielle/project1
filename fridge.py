x, y, z, m = map(int, input().split())

class holodoc:

    def __init__(self, name):
        self.milk = x
        self.meat = y
        self.cheese = z
        self.yummy = m


    def display_info(self):
        print(f"Milk: {self.milk}  Meat: {self.meat}  Cheese: {self.cheese} Yummy {self.yummy}")


fridge = holodoc("before")
fridge.milk = x
fridge.meat = y
fridge.cheese = z
fridge.yummy = m
fridge.display_info()


milk1,meat1,cheese1,yummy1 = map(int,input().split())


fridge1 = holodoc("after")
if fridge.milk + milk1 >= 0:
    fridge1.milk = fridge.milk + milk1
else: print("не хватает молочка")
if fridge.meat + meat1 >= 0:
    fridge1.meat = fridge.meat + meat1
else: print("не хватает мясца")
if fridge1.cheese + cheese1 >=0:
    fridge1.cheese = fridge.cheese +  cheese1
else: print("не хватает сырочка")
if fridge1.yummy + yummy1 >=0 :
    fridge1.yummy = fridge.yummy + yummy1
else: print("не хватает вкусняшек")

fridge1.display_info()
