import requests

def handler(event, context):
    try:
        res = requests.get(
            "https://1forge.com/forex-quotes/quotes",
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
