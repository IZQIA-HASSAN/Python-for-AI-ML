# class college:
#     def __init__(self, name , sem):
#         self.name = name
#         self.sem = sem
    
#     def semester(self):
#         return f'my coleg is {self.name} and i study in {self.sem}th semester  '

# x = college("GPGC" , 5)

# print(x.semester())

# class student(college):
#     def __init__(self , name , sem , year):
#         super().__init__(  name , sem)
#         self.graduationyear = year
        
#     def welcome(self):
#         return f'welcome {self.name} to the {self.sem} sem and you will now graduate in year {self.graduationyear}'
       

# x = student("mike" , 6 , 2018)
# print(x.welcome())
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
    pass
  

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("BMW" , "vehicle")
plane1 = Plane("Emirates" , "flying object")
boat1 = Boat("yatch" , "sailing object")

for x in (car1 , plane1 , boat1):
   print(x.brand)
   print(x.model)
   x.move()

