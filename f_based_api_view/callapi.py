import json 
import requests 

URL = "http://127.0.0.1:8000/"

def get_data(id = None ):
    obj = {}
    if id is not None:
        obj ={"id" : id}

    headers = {'content-Type' : "application/json"}
    json_data = json.dumps(obj)
    res = requests.get(url=URL , data=json_data , headers=headers)
    print(res.json())

# get_data()
get_data(1)


def post_data(name=None , roll=None , city=None):
    obj={
        "name" : name ,
        "roll" : roll ,
        "city" : city 
    }
    headers = {'content-Type' : "application/json"}
    json_data= json.dumps(obj)
    res = requests.post(url=URL , data=json_data , headers=headers)
    print(res.json())



# post_data("madhu sharma" , 123 , "banaras")