from django.shortcuts import render
from django.http import HttpResponse 
from .serializer import StudentSerializer 
from .models import Student
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf  import csrf_exempt 

import io 
# Create your views here.
@csrf_exempt
def home(request):
    if request.method == "GET":
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





    