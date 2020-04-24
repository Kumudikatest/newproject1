import requests

def handler(event, context):
    try:
        res = requests.get(
            "https://api.tink.com/api/v1/accounts/list",
            params={},
            headers={"Accept":"application/json"}
        )
        # your code goes here
        print(res)
    except BaseException as e:
        # error handling goes here
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
