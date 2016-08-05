from abc import ABCMeta, abstractmethod

class ITarget(metaclass=ABCMeta):
    @abstractmethod
    def request(self):
        pass

class Adaptee:
    def operation(self):
        pass

class ObjectAdapter(ITarget):
    def __init__(self):
        self._adaptee = Adaptee()
    
    def request(self):
        self._adaptee.operation();

class ClassAdapter(Adaptee, ITarget):
    def __init__(self):
        self._operation = self.operation

    def __getattribute__(self, name):
        if name == "operation":
            raise AttributeError("'ClassAdapter' object has no attribute '{}'".format(name));
        return super().__getattribute__(name)
        

    def request(self):
        self._operation()

target = ObjectAdapter()
target.request()

target2 = ClassAdapter()
target2.request()
target2.operation()