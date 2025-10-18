
import json

exampleJSON = '{"test1": "sample1", "test2":["Java", "C#", "Python"]}'

data = json.loads(exampleJSON)

print(data)



file = open("practice.txt")

# print(file.read())
print('**********************************')
# print(file.read(5))
print('**********************************')
# print(file.readline())
print('**********************************')
# print(file.readlines())


print('**********************************')

new_line = file.readline()

while new_line != "":
    print(new_line)
    new_line = file.readline()



