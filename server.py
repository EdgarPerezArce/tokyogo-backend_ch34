from flask import Flask
from data import me


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

app.run(debug=True)

