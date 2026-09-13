# class Outer:
#   def __init__(self):
#     self.name = "Emil"

#   class Inner:
#     def __init__(self, outer):
#       self.outer = outer

#     def display(self):
#       print(f"Outer class name: {self.outer.name}")

# outer = Outer()
# inner = outer.Inner(outer)
# inner.display()

# class college:
#     def __init__(self):
#         self.name = "college"

#     class inner:
#         def __init__(self , outer):
#             self.outer = outer
        
    
#         def display(self):
#             print(f'name os outer class is {self.outer.name}')
            
        

# outer = college()
# inn = outer.inner(outer)
# inn.display()

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.engine = self.Engine()

  class Engine:
    def __init__(self):
      self.status = "Off"

    def start(self):
      self.status = "Running"
      print("Engine started")

    def stop(self):
      self.status = "Off"
      print("Engine stopped")

  def drive(self):
    if self.engine.status == "Running":
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Start the engine first!")

car = Car("buggati" , "2026")
car.engine.start()
car.engine.stop()



fruits = ["applr" , "banana" , "mangoo"]

for index,fruit  in enumerate(fruits):
  print(index , fruit)



student = {
    "name" : "ahsan",
    "age" : 22,
    "work" : "work is being done",
  }

for key , value in student.items():
  print(key, value)

students = [
    {"name": "Ali", "marks": 80},
    {"name": "Sara", "marks": 95}
]

for i, student in enumerate(students, start=1):
    print(i, student["name"])


x = 1

while(x<5):
  print(x)
  x += 1

  
