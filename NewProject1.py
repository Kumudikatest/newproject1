import requests


def handler(event, context):
    
    try:
        res = requests.get(
            "http://demo.fintechsandpit.com/contact-for-access",
            params={},
            headers={"Accept":""}
        )
        print(res)
        # your code goes here
    except BaseException as e:
        # error handling goes here
        print(e)
        raise(e)
  
    return {"message": "Successfully executed"}
