# 48th Video

import requests

# this time our http method is Post
from post_http_rpayload3 import addBookPayload
from post_http_rpayload4 import buildPayLoadFromDB
from utilities.resources import *
from utilities.configurations import *
# '/Library/Addbook.php'
url = getConfig()['API']['endpoint'] + ApiResources.addBook
print(url)
headers = {'Content-Type': "application/json"}
query = 'select * from Books'
addBook_response = requests.post(url, json=buildPayLoadFromDB(query), headers=headers)

# The combination should be unique of the json code added otherwise it will state the book already exists
# We have given parameters here for post method and also took the first json code in Library API doc

print(addBook_response.json())   #{'Msg': 'Book Already Exists', 'ID': 'bnid3475'}

response_json = addBook_response.json()
print(type(response_json))   #<class 'dict'>

bookID = response_json['ID']
print(bookID)  #bnid3475

# Delete Book: ------------------------------------------------------------------------------------------------------------

response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

    "ID": bookID

}, headers={'Content-Type': "application/json"}
                                    )


print("Status Code:", response_deleteBook.status_code)

assert response_deleteBook.status_code == 200

res_json = response_deleteBook.json()

print(res_json["msg"])

assert res_json["msg"] == "book is successfully deleted"