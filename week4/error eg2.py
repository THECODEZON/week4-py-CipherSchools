class Mobile:
    def __init__(self,name):
        self.name = name

class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile, Mobile):
           self.mobiles.append(new_mobile)
        else:
            raise TypeError('galat mobile insert')   

oneplus = Mobile('one plus 6')
samsung = 'samsung galexy s9'

mobostore = MobileStore()
# mobostore.add_mobile(samsung)
mobostore.add_mobile(oneplus)
print(mobostore.mobiles)
mobo_phones = mobostore.mobiles
print(mobo_phones[0].name)
