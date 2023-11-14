import requests
import json 


URL = "http://127.0.0.1:8000/api/"

def get_data():
    headers = {'content_Type' : "application/json"}
    res = requests.get(url=URL+"1" , headers=headers)
    print(res.json())


# get_data()



def create(name=None , roll=None , city=None):
    obj = {}
    if name and roll and city is not None :
        obj = {
            'name' : name,
            'roll' : roll ,
            'city' : city 
        }
        headers = {
            'content-Type' : 'application/json'
        }
        json_data= json.dumps(obj)
        res = requests.post(url=URL , headers=headers , data=json_data)
        print(res.json())



# create("amulay" , 123 , "madhyapradesh")

def dlt(id=None):
    if id is not None:
        obj = {
            'id' : id
        }

        json_data=json.dumps(obj)
        headers={
            'content-Type' : "application/json"
        }
        res = requests.delete(url=URL , headers=headers , data=json_data)
        print(res.json())


dlt(2)