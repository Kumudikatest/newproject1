import requests
import json

def handler(event, context):
    
    try:
        res = requests.post(
            "https://sandbox.plaid.com/auth/get",
            params={},
            headers={"Accept":"application/json","Content-Type":"application/json"},
            data=json.dumps({"test":"1"})
        )
        # your code goes here
        print(res)
    except BaseException as e:
        # error handling goes here
        print(e)
        raise(e)
  
    return {"message": "Successfully executed"}
