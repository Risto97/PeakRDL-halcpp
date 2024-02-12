class BaseClass():
    def __init__(self):
        self.my_var0 = 1
        self.my_var1 = 2

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        self.my_var2 = 3

        self.mydict = {}

    def print_vars(self):
        print(self.my_var0)
        print(self.my_var1)
        print(self.my_var2)

from abc import ABC, abstractmethod

class MyBaseClassAbstract(ABC):
    def __init__(self):
        self.my_var0 = 1
        self.my_var1 = 2
    @abstractmethod
    def abstract_method(self):
        pass

class DerivedClassAbstract(MyBaseClassAbstract):
    def __init__(self):
        super().__init__()
        self.my_var2 = 3
    def my_method(self):
        print('my_method call')
    def abstract_method(self):
        print('Abstract method call')
    def print_vars(self):
        print(self.my_var0)
        print(self.my_var1)
        print(self.my_var2)


DerivedClass0 = DerivedClass()

DerivedClass0.print_vars()

# AbstracClass0 = MyBaseClassAbstract()
AbstracClass1 = DerivedClassAbstract()
AbstracClass1.print_vars()

classdict = DerivedClass0.mydict

classdict['myentry'] = 'myvalue'

print(DerivedClass0.mydict)
