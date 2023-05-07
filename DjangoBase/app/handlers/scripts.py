import requests
import json

def insert_products():
    try:
        base_url = 'http://localhost:8000' 
        data = json.load(open('products.json', 'r'))
        products = data.get('products')
        for product in products:
            headers = {
                'Content-Type': "application/json"
            }
            payload = {
                "reference": product.get("reference"),
                "name": product.get("name"),
                "volume": product.get("volume"),
                "created": product.get("created")

            }

            response = requests.request("PUT", url=base_url + '/valerdat/products', headers=headers, data=json.dumps(payload))
    except Exception as e:
        print(e)



        