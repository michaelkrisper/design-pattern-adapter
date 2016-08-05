class Adaptee:
    def operation(self):
        print("Adaptee.operation() called")

class ClassAdapter(Adaptee):
    def request(self):
        self.operation()

class ObjectAdapter():
    def __init__(self):
        self._adaptee = Adaptee()
    
    def request(self):
        self._adaptee.operation();

target = ObjectAdapter()
target.request()