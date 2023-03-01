from flask import Flask,abort, request
from data import me,mock_catalog
from config import db
from bson import ObjectId
import json

app = Flask(__name__) # creating a new instance, similar to new Task in JS

@app.get("/")
def home():
    return "Hello World!"

@app.get("/about")
def about():
    return "Edgar Perez"

@app.get("/contact/me")
def contactme():
    return "perezarcededgar@gmail.com"


################################################
############### API -> JSON ####################
################################################
@app.get("/api/developer")
def developer():
    return json.dumps(me)#parse me into a jason string

# get /api/developer/address
# STREET #NUM, CITY, ZIPCODE

@app.get("/api/developer/address")
def developer_address():
    address = me["address"]
    # return address["street"] + " #" + str(address["number"]) + ", " + address["city"] + ", " + address["zip"]
    # f string
    return f'{address["street"]} #{address["number"]}, {address["city"]}, {address["zip"]}'

def fix_id(obj):
    obj["_id"] = str(obj["_id"])

# get /api/catalog
# return the list of products as JSSON
@app.get("/api/catalog")
def tokyogo_catalog():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)

    return json.dumps(results)

@app.post("/api/catalog")
def save_product():
    data = request.get_json()
    db.products.insert_one(data)
    fix_id(data)
    return json.dumps(data)

@app.get("/api/catalog/count")
def tokyogo_count():
    total = db.products.count_documents({})
    return json.dumps(total)


@app.get("/api/catagory/<cat>")
def prod_by_catagory(cat):
    cursor = db.products.find({"category" : cat})
    results = []

    for prod in cursor:
        fix_id(prod)
        results.append(prod)


    return json.dumps(results)

@app.get("/api/product/<id>")
def prod_by_id(id):
    _id = ObjectId(id)
    prod = db.products.find_one({"_id" : _id})
    if prod is None:
        return abort(404, "Invalid id")
    
    fix_id(prod)
    return json.dumps(prod)

               

@app.get("/api/product/search/<text>")
def search_product(text):
    #search the product whose title containes the text (case insensitive)
    cursor = db.products.find({ "title" : { "$regex": text, "$options": "1"} })
    results = []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)

    return json.dumps(results)

@app.get("/api/categories")
def get_catagories():
    cursor = db.products.distinct("category")
    return json.dumps(list(cursor))

@app.get("/api/total")
def get_total():
    total = 0
    for prod in mock_catalog:
        total += prod["price"]

    return json.dumps(total)

@app.get("/api/cheaper/<price>")
def get_cheaper(price):
        price = float(price)
        results = []
        for prod in mock_catalog:
            if prod["price"] <= price:
                results.append(prod)

        return json.dumps(results)


# challenge
# find and return the cheapest product

# create a cheapest = mock_catalog[0]
# for loop to travel the list
# get every prod from the list
# if the price of prod is lower than the price of cheapest
# then update cheapest to be the prod (cheapest = prod)

    
app.run(debug=True)

