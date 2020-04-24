import requests
import json

def handler(event, context):
    try:
        res = requests.post(
            "https://api.sandbox.paypal.com/v2/checkout/orders",
            params={},
            headers={"Accept":"application/json","Content-Type":"application/json"},
            data=json.dumps({"Test":"1"})
        )
        # your code goes here
        print(res)
    except BaseException as e:
        # error handling goes here
        print(e)
        raise(e)
  
    return {"message": "Successfully executed"}
