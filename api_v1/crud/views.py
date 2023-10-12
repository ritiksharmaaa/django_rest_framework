from django.shortcuts import render
from django.http import HttpResponse 
from .serializer import StudentSerializer 
from .models import Student
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf  import csrf_exempt 

import io 



#  you can use class api view for not write this metthod === this or that is easily handel in api views .
# Create your views here.
@csrf_exempt
def home(request):
    # print(request.user)
    if request.method == "GET":
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id' , None)
        if id is not None:
            obj = Student.objects.get(id=id)
            serilizer = StudentSerializer(obj)
            json_data = JSONRenderer().render(serilizer.data)
             # print(json_data)
            return HttpResponse(json_data , content_type="application/json")
        else :
              obj = Student.objects.all()
              serilizer = StudentSerializer(obj , many=True)
              json_data = JSONRenderer().render(serilizer.data)
              # print(json_data) 
              return HttpResponse(json_data , content_type="application/json")

    if request.method == "POST":
        json_data = request.body 
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        d_serializer = StudentSerializer(data=pythondata) # this can convert native data to complex data 
        if  d_serializer.is_valid():
            d_serializer.save()
            # give back response to give sign that data is created 
            msg = {
                'msg' : 'data created as well as inserted'
            }
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data , content_type="application/json")
        else:
            msg = {
                'error' : d_serializer.errors
            }
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data , content_type="application/json")
    

    # update 
    if request.method == "PUT":
        json_data = request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serilizer = StudentSerializer(stu, data=python_data , partial=True)
        if  serilizer.is_valid():
            serilizer.save()
            print(" data updated ..............................................")
            msg = {
                'updated_data' : serilizer.validated_data
            }
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data , content_type="application/json")
        else:
            json_data = JSONRenderer().render(serilizer.errors) 
            return HttpResponse(json_data , content_type="application/json")


    # delete data 
    if request.method =="DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        msg ={
            'msg' : f"the{id} which you want to deleted is now deleted "
        }
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data , content_type="application/json")
    






    