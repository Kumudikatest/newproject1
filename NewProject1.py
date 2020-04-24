import requests

def handler(event, context):
    
    try:
        res = requests.get(
            "https://play.railsbank.com/v1/customer/version",
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
