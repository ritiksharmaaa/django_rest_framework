from django.shortcuts import render
from django.http import HttpResponse 
import io 
from . models import Student 
from .serializer import StudentSerilizer 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt 
# io.BytesIO

# Create your views here.

@csrf_exempt
def home(request):
    if request.method == "GET":
        json_data = request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id" , None )
        if id is not None :
            stu = Student.objects.get(pk=id)
            serializer = StudentSerilizer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content_type="application/json")
        
        pythondata = StudentSerilizer(data , many=True)
        data = Student.objects.all()
        json_data = JSONRenderer().render(pythondata.data)
        print(json_data)
        # print(pythondata)
        return HttpResponse(json_data  ,content_type= "application/json")
    
    if request.method == "POST":
        json_data = request.body 
        stream = io.BytesIO(json_data)
        pd = JSONParser().parse(stream)
        d_serializer = StudentSerilizer(data=pd)
        if d_serializer.is_valid():
            d_serializer.save()
            msg = {
                'msg' : "data created succefully ",
                'data' : d_serializer.validated_data
            }
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data , content_type="application/json")
        json_data = JSONParser().parse(d_serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
        

    if request.method == "PUT":
        json_data = request.body 
        stream = io.BytesIO(json_data)
        pd = JSONParser().parse(stream)
        id = pd.get("id")
        stu = Student.objects.get(pk=id)
        d_sea_update = StudentSerilizer(stu , data=pd , partial=True)
        if d_sea_update.is_valid():
            d_sea_update.save()
            msg = {
                'msg' : f" your data is successfully updated  {d_sea_update.validated_data}"
            }
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data , content_type="applcation/json")
        else:
            msg = {
                'msg' : d_sea_update.errors
            }
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data , content_type="application/json")


    if request.method == "DELETE":
        json_data = request.body 
        stream = io.BytesIO(json_data)
        pd = JSONParser().parse(stream)

        id = pd.get("id")
        Student.objects.get(id=id).delete()
        msg={
            'msg' :  " Your data is deleted Successfully !! "

        }

        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data , content_type="application/json")




