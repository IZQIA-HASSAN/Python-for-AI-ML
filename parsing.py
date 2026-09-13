import json
import requests

json_string = '{"name" : "ahmed" , "age" : 20}'
data  = json.loads(json_string)
print(type(data["name"]))

python_dict = {"city" : "lahore" , "population" : 10000000}
json_text = json.dumps(python_dict)
print(json_text)

data = '''
{
  "name": "Sara",
  "age": 22,
  "is_student": true,
  "courses": ["Math", "CS", "Physics"],
  "address": {
    "city": "Lahore",
    "zip": "54000"
  }
}
'''

python_obj = json.loads(data)
print(python_obj)

print(python_obj["name"] )
print(python_obj["age"])

for c in python_obj["courses"]:
    print(c)

addres = python_obj["address"]

for key , value in addres.items():
    print(key , value)

print(python_obj["address"]["city"])

repsonse = requests.get("https://jsonplaceholder.typicode.com/users/1")
data = repsonse.json()
print(data["name"])

for key , value in data.items():
    print(f"{key} : {value}")