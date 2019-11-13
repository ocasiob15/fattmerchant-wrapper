from flask import Blueprint, request
from client.fattmerchant_client import FattmerchantApi
import json

store = Blueprint("store_controller", __name__)

with open('config.json') as config:
    data = json.load(config)


@store.route("/store/catalog", methods=['GET'])
def store_get_catalog():
    api = FattmerchantApi()
    return json.dumps(api.get_catalog_items(data['fattmerchant']['apiKey']))


@store.route("/store/checkout/invoice", methods=['POST'])
def store_create_invoice():
    api = FattmerchantApi()
    return json.dumps(api.create_invoice(request.get_json(), data['fattmerchant']['apiKey']))

