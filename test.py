# # print("hello" , "wrold")

# # my_age = 17
# # my_name = "meerali"
# # print(my_age , my_name)

# # print(type(my_age))

# # account_balance = 12

# # print(isinstance(account_balance , (int , float)))

# # # strings 

# # name  = "hassan"

# # namer  = '''my name is hasan 
# # and i am learning python '''

# # print(name , namer)

# # quote = "quaid said 'work work and stop'"
# # print(quote)

# # msg= "it's a sunny day"
# # msg2 = "she said , \"hello!\""
# # print(msg , msg2)\

# # print("sunny" in msg)


# # mystring = "muhammad"
# # print(len(mystring))

# # print(mystring[-1])

# # sound = "ha"
# # anothersound = 3
# # fullsound = sound * anothersound
# # print(fullsound)

# # str1 = "izqia"
# # str2 = "hassan"
# # str4 = 23
# # str3 = str1 + str2
# # str5 = str1 + str4 
# # print(str5)
# # print(str3)

# name = "johndoe"
# age  = 18
# # fullname = "my name is " + name + " and my age is " + str(age)
# # print(fullname) 

# name_and_age = name
# name_and_age += str(age)

# print(name_and_age)

# interpolation = f'my nameis {name} and my age is {age} , good bye'
# print(interpolation)

# # slice in pytohn 
# my_str = "Hello world"
# print(my_str[2:-1])
# print(my_str[:-1])
# print(my_str[8:])
# print(my_str[:])
# print(my_str[0:8:2])
# print(my_str[::-1])

# # some common string methods

# school = "post graduate college mansehra "

# uppercase = school.upper()
# lower = school.lower()
# # print(uppercase)
# print(lower)

# striping = school.strip()
# # works same as trim in javascript
# print(striping)  

# replaced = school.replace("post" , "mansehra")
# print(replaced)

# spliting = school.split()
# print(spliting)

# mylist = ["table" , "tennis"]
# joined = ' '.join(mylist)
# print(joined)
# # print(mylist.join(mylist))

# start = school.startswith(" post")
# # print(start)

# ends = school.endswith(" ")
# print(ends)

# finder = school.find("mansehra")
# print(finder)

# counter = school.count("a")
# print(counter)

# cap = school.capitalize()
# print(cap)

# upp = school.isupper()
# print(upp)

# low = school.islower()
# print(low)

# capital = school.title()
# print(capital)


# age  = 13
# name = "ahmed khan"

# if age > 13 :
#     print("age is not verified")
# elif age <= 13:
#         print("age is eligible")
# else:
#         print("okay they are working")

# identation matters alot in python

# def sum (a, b):
#     return a +  b 

# sum = sum(3, 4)
# print(sum)    

# local scope
# def my_fun():
#     my_var = 10
#     print(my_var)

# my_fun()

# print(my-var)

# Enclosing scope

# def outer_fun():
#     msg = "outer function"
#     res = ""
#     def inner_fun():
#         nonlocal res
#         res = "this is inner non-local variable"
#         print(msg)

#     inner_fun()
#     print(res)

# outer_fun()



num = 10

# def fun():
#     print("this is inner fun" , num)

#     def fun2():
#         print("this is inner2" , num)

#     fun2()

#     # fun2()

# fun()    


my_var = 10  # A global variable

# def change_var():
#     global my_var  # Allows modification of a global variable
#     my_var = 20

# change_var()

# print(my_var)


# def apply_discount(price  , discount):
#     if not (isinstance(price , int) or isinstance(price , float)):
#         return "The price should be a number"

#     if not isinstance(discount, (int , float)):
#         return "The discount should be a number"

#     if price <=0 :
#         return "The price should be greater than 0"

#     if discount <0 or discount >100:
#         return "The discount should be between 0 and 100" 

#     return price-(price * discount/100)


# apply_discount(100 , 20)
# apply_discount(200 , 50)
# apply_discount(50 , 0)
# apply_discount(0 , 50)
# # apply_discount(90 , "a")
# apply_discount(74.5, 100)
# apply_discount(74.5, 20.0)


# loops in python 

# programming_languages = ['rust' , 'python' , 'cpp' , 'js']

# for l in programming_languages:
#     print(l)

# for char in "meerali":
#     print(char)

# categries = ["low" , "high" , "intermediate"]
# foods = ["carrot" , "cucumber" , "pineapple"]

# for c in categries:
#     for f in foods:
        # print(c , f)





# devs = ['fawas' , 'ali'  , 'ahmed']

# for d in devs:
#  if d == 'ali':
#     continue
#  print(d)

# developer_names = ['Jess', 'Naomi', 'Tom']

# for developer in developer_names:
#     if developer == 'Naomi':
#         continue
#     print(developer)


# words = ['sky' , 'apple' , 'rythm' , 'fly' , 'orange']

# for word in words:
#     for letter in word:
#         if letter.lower() in 'aeiou':
#             print(f"'{word}' contains vowel '{letter}'")
#             break
#     else:
#         print(f"'{word}' has no vowels")


# foods = ['biryani' , 'burger']

# for f in foods:
#     for i in f:
#         if i.lower() in "aeiou":
#             print(f"'{f}' constains a vowel '{i}'")
#             break
#     else:
#         print(f"'{f}' has no vowel")


# for num in range(40 , 0 , -10):
#     print(num)

# numbers = list(range(2,20,2))
# print(numbers)

# languages = ["arabic" , "hindko" , "spanish "]

# print(list(enumerate(languages)))

# for index , language in enumerate(languages, 2):
#     print(index , language)


# temp = [0 , 10 , 20 , 30 , 40]

# def to_farenhiet(temp):

#     return (temp* 9/5) + 32



# farenhiet = list(map(to_farenhiet , temp))
# print(farenhiet)


numbers = [1,2,3,4,5]
even_numbers = list(filter(lambda n:n%2 == 0 , numbers))
print(even_numbers)

