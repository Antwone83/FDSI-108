from flask import Flask
from mock_data import catalog
import json


app = Flask(__name__)
me = {
    "name": "Antwone",
    "last": "Adams",
    "age": 38,
    "hobbies": [],
    "address": {"street": "Southview", "number": "83", "city": "Springfield"},
}


@app.route("/", methods=["GET"])
def home():
    return "Hello from Python"


@app.route("/test")
def any_name():
    return "I'm a test function."


@app.route("/about")
def about():
    return me["name"] + "  " + me["last"]

    # ---------------------------------------------------------------
    # ----------------------  API ENDPOINTS  ------------------------
    # ---------------------------------------------------------------


@app.route("/api/catalog")
def get_catalog():
    # TODO: read the catalog
    return json.dumps(catalog)


@app.route("/api/cheapest")
def get_cheapest():

    cheap = catalog[0]
    for product in catalog:
        if product["price"] < cheap["price"]:
            cheap = product

    # find the cheapest product on the catalog list
    # 1 - travel the list with for loop
    # 2 - printout the price on the console

    # return it as json
    return json.dumps(cheap)


@app.route("/api/product/<id>")
def get_product(id):

    for product in catalog:
        if product["_id"] == id:
            return json.dumps(product)

    return "NOT FOUND"

# start the server
app.run(debug=True)
