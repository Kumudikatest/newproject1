import requests

def handler(event, context):

    try:
        res = requests.get(
            "https://api.stripe.com/v1/account",
            params={"expand":"time"},
            headers={"Accept":"application/json"}
        )
        # your code goes here
        print(res)
    except BaseException as e:
        # error handling goes here
        raise(e)
        print(e)
  
    return {"message": "Successfully executed"}
