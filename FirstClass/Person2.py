class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Bad Name")


person = Person("Jon")
print(person.name)
person.name = "Jonathan"
print(person.name)

person2 = Person("Jess")
print(person2.name)