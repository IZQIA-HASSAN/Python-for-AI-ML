try:
    x = 10/0
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("division successful : " , x)
finally:
    print("this block always runs")

try:
    number = int('abc')
    result = 10/number
except ValueError:
    print('this was not a valid number')
except ZeroDivisionError:
    print("canont divide by zero")    

try:
    x= 1/0
except ZeroDivisionError as e:
    print(f'Error Occured : {e}')

try:
    number = int(input('Enter a number: '))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occurred: {e}')


def check_age(age):
    if age < 0 :
        raise ValueError("age cannot be negative")
    return age
try:
    check_age(-5)
except ValueError as e:
    print(f'Error:{e}')
