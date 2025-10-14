
class Person :
    def __init__(self,name) :
        self._name = name
        
    # accessor
    def get_name(self) :
        return self._name
        
    def set_name(self,name) :
        if isinstance(name,str) and len(name) > 0 :
            self._name = name
        else :
            raise ValueError("Invalid Name")
            
person = Person("Jon")
print(person.get_name())
person.set_name("Jonathan")
print(person.get_name())

person._name = 12313123
print(person._name)

