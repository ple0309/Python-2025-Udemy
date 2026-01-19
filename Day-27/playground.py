def add(*args):
    total = 0
    for n in args:
        total += n
    return total

# print(add(1,2,3,4,4,5))

def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3, multiply=5)

#**********************************************************************
class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-8")
print(my_car.model)
#**********************************************************************
#Output Error Because it does not have model argument
# class Car:
#     def __init__(self,**kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#
# my_car = Car(make="Nissan")
# print(my_car.model)
#**********************************************************************
#Output None instead of Error by using get method
# class Car:
#     def __init__(self,**kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#
# my_car = Car(make="Nissan")
# print(my_car.model)