import requests 
import json 



URL = "http://127.0.0.1:8000/"


def get_data(id=None):
    obj = {}
    if id is not None:
        obj = {'id' : id }
    json_data = json.dumps(obj)
    res = requests.get(url=URL , data=json_data)
    print(res.json())
    


# get_data()


def create(name , roll , city):
    if name and roll and city == None :
        print(" sorry give validate data !! ")
    obj = {
        "name" : str(name),
        "roll" : int(roll),
        "city" : str(city)
    }
    json_data = json.dumps(obj)
    res = requests.post(url=URL , data=json_data)
    print(res.json())



# create("hardik" , 107 , "chandigar ")



def update(id , name=None , roll=None , city=None ):

    obj={
        "id" : id ,
        'name' : str(name),
        "roll" : int(roll),
        "city" : str(city)
    }

    json_data = json.dumps(obj)
    res = requests.put(url=URL , data=json_data)
    print(res.json())





# update(3 , "amulya rattan" , 108 , "madhavpur")



def delete(id):
    obj={
        "id": id
    }

    json_data = json.dumps(obj)
    res = requests.delete(url=URL , data=json_data)
    print(res.json())


delete(2)