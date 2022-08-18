def add(*args):
    soma = sum(args)
    return soma

print(add(10, 42, 73))


def test(*args):
    print(args)
test(1, 2, 3, 5)


def calculate(n, **kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
     #   print(key)
    #    print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.seats = kw.get("seats")
        self.colour = kw.get("colour")


my_car = Car(make="Ferrari")
print(my_car.make)