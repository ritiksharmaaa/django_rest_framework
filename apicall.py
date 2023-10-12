import requests 
import json 
# print(json)
# print(requests)



# first way to calll api 
# URL = "http://127.0.0.1:8000/crud/"

# data = {
# 'name': 'mohan',
#     'roll': 104,
#     'city' : 'world'
# }

# json_data = json.dumps(data)

# res = requests.post(url = URL , data= json_data)
# print(res.json())


#from second way to request an api !: - -----------------------------------------

# URL = 'http://127.0.0.1:8000/crud/'
# def get_data(id=None):
#     data={} #when this is not it will give you all data 
#     if id is not None :
#         data={'id' : id}
#     else:
#         print("plese give id to function ")
#     json_data = json.dumps(data)
#     r = requests.get(url=URL , data=json_data)
#     print(r.json())


# get_data(3)
# get_data()



# put 

URL = 'http://127.0.0.1:8000/crud/'
def update_data(id=None):
    data={
        'id' : 3 ,
        'name':'madan',
        # we comment to check paritail data update 
        # 'roll' : 107,
        'city' :'delhi',
    } #when this is not it will give you all data 
    print("we are updating ......")
    json_data = json.dumps(data)
    r = requests.put(url=URL , data=json_data)
    print(r.json())


# update_data()



# del 



def del_data(id):
    data={'id' : id }
    json_data = json.dumps(data)
    res = requests.delete(url=URL , data=json_data)
    print(res.json())


del_data(2)





