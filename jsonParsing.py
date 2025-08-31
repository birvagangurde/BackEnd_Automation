import json

courses = '{"name": "RahulShetty", "languages": ["Java", "Python"]}'

# Loads method parse json string and returns dict

dict_courses = json.loads(courses)

print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

# get me the first language taught by trainer

list_language = dict_courses['languages']
print(type(list_language))
print(list_language[0])
print(dict_courses['languages'][0])

# This is one way of json parsing
