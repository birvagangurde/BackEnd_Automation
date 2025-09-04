import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName': 'Rahul Shetty2'}, )

print(response.text)
print(type(response.text))

dict_response = json.loads(response.text)
print(dict_response)
print(type(dict_response))

print(dict_response[0]['isbn'])


json_response = response.json()
print(type(json_response))



