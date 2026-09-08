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
