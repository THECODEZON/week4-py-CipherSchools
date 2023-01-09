#raise error exple 1
#NotImpelement
#abstract method

class Animal :
    def __init__(self,name):
        self.name = name


    def sound(self):
        raise NotImplementedError()

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'bhow bhow'
            
class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'mai aoooo'

doggy = Dog('swati','rhu')
print(doggy.sound())

doggy = ('swati','rhu')
print(doggy.sound())