
import json

x = '{"Name" : "Bob" , "Age" : 30, "City" : "New York" }'
y = json.loads(x)
print(type(y))
print(y)

X = {"Name" : "John", "Age" : 40, "City" : "Bangalore"} #a python object(dict)
y = json. dumps(X) # Convert into json
print(y) # Result is a json string 


person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)
print( person_dict)
print(person_dict['languages']) 


person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)
print(person_json)
