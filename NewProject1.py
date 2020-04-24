import requests

def handler(event, context):
    try:
        res = requests.get(
            "https://api.sandbox.transferwise.tech/v1/addresses",
            params={"profile":"1"},
            headers={"Accept":"application/json"}
        )
        # your code goes here
        print(res)
    except BaseException as e:
        # error handling goes here
        print(e)
        raise(e)
  
    return {"message": "Successfully executed"}
