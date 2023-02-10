from flask import Flask,abort
from data import me,mock_catalog

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

# get /api/catalog
# return the list of products as JSSON
@app.get("/api/catalog")
def tokyogo_catalog():
    return json.dumps(mock_catalog)

@app.get("/api/catalog/count")
def tokyogo_count():
    count = len(mock_catalog)
    return json.dumps(count)


@app.get("/api/catagory/<shirts>")
def prod_by_catagory(shirts):
    results = []
    for prod in mock_catalog:
        if prod["category"] == shirts:
            results.append(prod)


    return json.dumps(results)

@app.get("/api/product/<id>")
def prod_by_id(id):
    for prod in mock_catalog:
        if prod["_id"] == id:
            return json.dumps(prod) 

    return abort(404, "Invalid id")           

@app.get("/api/product/search/<text>")
def search_product(text):
    results = []
    for prod in mock_catalog:
        if text.lower() in prod["title"].lower():
            results.append(prod)

    return json.dumps(results)

@app.get("/api/categories")
def get_catagories():
   results = []
   for prod in mock_catalog:
       cat + prod["category"]
   
   


app.run(debug=True)

