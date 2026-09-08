# class Person:
#     def __init__(self , name , age):
#         self.name = name
#         self.__age = age

#     def get_age(self):
#         return self.__age

#     def set_age(self , age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("age must be greter then 0")

# p1 = Person("Email" , 24)
# print(p1.name)
# print(p1.get_age())

# p1.set_age(4)
# print(p1.get_age())

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary)


class calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num,(int, float)):
            return False
        return True

    def add(self, num):

        if self.__validate(num):
            self.result += num
        else:
            print("invalid number")


calc = calculator()
calc.add(10)
print(calc.result)

        
