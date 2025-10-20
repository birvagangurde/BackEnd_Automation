import requests
from behave import *
from post_http_rpayload4 import *
from utilities.resources import *
from utilities.configurations import *


@given('the Book details which needs to be added to Library')
def step_impl(context):
    #
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload("mbrode", "4373");


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad , headers=context.headers, )


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.bookId = response_json['ID']
    print(context.bookId)
    print(response_json["Msg"])
    assert response_json["Msg"] == "successfully added"