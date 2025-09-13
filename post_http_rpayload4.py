# 48th Video

from utilities.configurations2 import *


def addBookPayload(isbn):
    body = {

        "name": "Test Book for Matts practice",
        "isbn": isbn,
        "aisle": "2re57",
        "author": "John foe"
    }
    return body


def buildPayLoadFromDB(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]

    return addBody
