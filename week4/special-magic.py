# special magic method / dunder method
# operator overloading
# polymorphism

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price  

    def phone_name(self):
        return f"{self.brand} {self.model}"

 # str , repr

    def __str__(self):
        return f"{self.brand} {self.model} "

    # def __repr__(self):
    #     return f"{self.brand} {self.model} "

    def __repr__(self):
        return f"phone({self.brand},{self.model},{self.price})"

    def __len__(self):
        return len(self.phone_name)

    def __add__ (self, other):
        return  self.price + other.price




my_phone = Phone('nokia','1100',1000)
my_phone2 = Phone('nokia','1100',8000)
print(my_phone)        
# print(str(my_phone))        
print(repr(my_phone)) 

print(my_phone + my_phone2)




# l = [1,2,3]
# print(len(l))
# t = (1 ,2 , 3)
# s = "deepa"
# print(len(s))
# print(len(t))


# 2 + 3 = 5
#'abc' + 'def' = 'abcdef'



#many forms
 
class SmartPhone(Phone):
    def __init__(self, brand, model, price):
        super().__init__(brand,model,price)
        # self.camera = camera

    def phone_name(self):
        return f"f{self.brand} {self.model} and price is `{self.price}"    
   
my_phone = Phone('nokia','1100',1000)
my_phone2 = Phone('nokia','1100',8000)
my_smartphone = SmartPhone('oneplus','5t',33000,)   
print(my_smartphone.phone_name())
print(my_phone.phone_name())


