# class ClassName:
#     def __init__(self , age , name):
#         self.name = name
#         self.age = age

#     def sample_method(self):
#         print(self.name.upper())


# class Dog:
#     def __init__(self , age , name):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name.upper()} says woof woof!")

# object_1 = Dog(23 , "bull")
# object_2 = Dog(25 , "bulliesy")

# object_1.bark()
# # object_2.bark()

# class school:
#     students = "too many use less students"

#     def __init__(self , name):
#         self.name = name

# print(school.students)

# student1 = school("izqia")
# # print(student1.name)
# # print(student1.students)

# class car:
#     def __init__(self, model , color):
#         self.model = model
#         self.color = color

# car1 = car("BMW" , "Green")
# car2 = car("Civic" , "Red")

# print(car1.model)
# print(car2.model)

# class dog:
#     species = "french bulldog"

#     def __init__(self , name ):
#         self.name = name

#     def bark(self):
#             return f"{self.name} says woof woof"


# jack = dog("Jack")
# bill = dog("bill")
# print(dog.species)

# print(jack.bark())
# print(bill.bark())

# class book:
#     def __init__(self , title , pages):
#         self.title = title
#         self.pages = pages

#     def __len__(self):
#         return self.pages
    
#     def __str__(self):
#         return f"{self.title} has {self.pages} pages"

#     def __eq__(self , other):
#         return self.pages == other.pages

    

# book1 = book("built with no fear" , 400)
# book2 = book("built with fear" , 500)

# print(len(book1))
# print(len(book2))
# print(str(book1))
# print(str(book2))

# print(book1 == book2)


# class Cart:
#    def __init__(self):
#        self.items = []

#    def add(self, item):
#        self.items.append(item)

#    def remove(self, item):
#        if item in self.items:
#            self.items.remove(item)
#        else:
#            print(f'{item} is not in cart')

#    def list_items(self):
#        return self.items

#    def __len__(self):
#        return len(self.items)

#    def __getitem__(self, index):
#        return self.items[index]

#    def __contains__(self, item):
#        return item in self.items

#    def __iter__(self):
#        return iter(self.items)
         

# cart = Cart()
# cart.add('Laptop')
# cart.add('Wireless mouse')
# cart.add('Ergo keyboard')
# cart.add('Monitor')

# for item in cart:
#    print(item)

#    print(len(cart))

# cart.remove('Monitor')

# class person:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age

# Person = person('john doe' , 23)
# attr_name = input("Enter the attribiute you want to see")
# print(getattr(Person , attr_name , 'attribute not found'))

# class adder :
#     def add(self ,a,b):
#         return a + b

# cal = adder()
# print(cal.add(5,6))


# class names:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age

# nam = names('izqia' , 22)

# for attr in dir(nam):
#     if not attr.startswith('__') and not callable(getattr(nam , attr)):
#         value = getattr(nam , attr)
#         print(f'{attr} : {value}')

    
