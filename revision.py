# scores = [55, 82, 91, 47, 63, 78, 90, 34, 88, 71]

# for index , value in enumerate(scores):
#     if value >= 60 :
#         print(f"index {index} : {value} you are passed ")

# total = 0
# for  value in scores:
#     total += value
# average = total/len(scores)
# print(f"total average is {average}")

# highest_score = scores[0]
# lowest_score = scores[0]

# for value in scores:
#     if value > highest_score:
#         highest_score = value
        
#     if value < lowest_score:
#         lowest_score = value
        

# print(f"loweest score is {lowest_score}")
# print(f"highest score is {highest_score}")



# student = {"name": "Ali", "age": 20, "grades": [85, 90, 78]}

# print(student["grades"])

# total = 0


# for marks in student["grades"]:
#     total += marks

# average = total/len(student["grades"])

# student["average"] = average

# for key , value in student.items():
#     print(f"{key} is/are {value}")


# class_a = {"Ali", "Sara", "Bilal", "Ayesha"}
# class_b = {"Bilal", "Hina", "Ali", "Zara"}

# print(class_a & class_b)
# print(class_a - class_b)
# print(class_a | class_b)

# union = class_a | class_b
# tuples = sorted(union)
# print(tuple(tuples))


class Animal:
    def __init__(self , name , sound):
        self.name  = name
        self.sound = sound

    def makesound(self):
        print(f"{self.name} says {self.sound}")


class dog(Animal):
    def fetch(self ):
        print(f"{self.name} is fetching the ball")


class cat(Animal):
    def makesound(self):
        print(f"{self.name} says hehe {self.sound}")



# obj_1 = Animal()
c = cat("cat" , "meow")
c.makesound()

class puppy(dog):
    def __init__(self , name , sound  , age):
        super().__init__(name , sound)
        self.age  = age

p = puppy("marie" , "boo boo" , 23)
p.makesound()
p.fetch()
print(p.age)