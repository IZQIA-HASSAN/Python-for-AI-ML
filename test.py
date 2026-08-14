# print("hello" , "wrold")

# my_age = 17
# my_name = "meerali"
# print(my_age , my_name)

# print(type(my_age))

# account_balance = 12

# print(isinstance(account_balance , (int , float)))

# # strings 

# name  = "hassan"

# namer  = '''my name is hasan 
# and i am learning python '''

# print(name , namer)

# quote = "quaid said 'work work and stop'"
# print(quote)

# msg= "it's a sunny day"
# msg2 = "she said , \"hello!\""
# print(msg , msg2)\

# print("sunny" in msg)


# mystring = "muhammad"
# print(len(mystring))

# print(mystring[-1])

# sound = "ha"
# anothersound = 3
# fullsound = sound * anothersound
# print(fullsound)

# str1 = "izqia"
# str2 = "hassan"
# str4 = 23
# str3 = str1 + str2
# str5 = str1 + str4 
# print(str5)
# print(str3)

name = "johndoe"
age  = 18
# fullname = "my name is " + name + " and my age is " + str(age)
# print(fullname) 

name_and_age = name
name_and_age += str(age)

print(name_and_age)

interpolation = f'my nameis {name} and my age is {age} , good bye'
print(interpolation)

# slice in pytohn 
my_str = "Hello world"
print(my_str[2:-1])
print(my_str[:-1])
print(my_str[8:])
print(my_str[:])
print(my_str[0:8:2])
print(my_str[::-1])

# some common string methods

school = "post graduate college mansehra "

uppercase = school.upper()
lower = school.lower()
print(uppercase)
print(lower)

striping = school.strip()
# works same as trim in javascript
print(striping)  

replaced = school.replace("post" , "mansehra")
print(replaced)

spliting = school.split()
print(spliting)

mylist = ["table" , "tennis"]
joined = ' '.join(mylist)
print(joined)
# print(mylist.join(mylist))

start = school.startswith(" post")
print(start)

ends = school.endswith(" ")
print(ends)

finder = school.find("mansehra")
print(finder)

counter = school.count("a")
print(counter)

cap = school.capitalize()
print(cap)

upp = school.isupper()
print(upp)

low = school.islower()
print(low)

capital = school.title()
print(capital)

