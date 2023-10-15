from django.shortcuts import render
from django.http import HttpResponse 

from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .serializer import StudentSerializer
from . models import Student

# # Create your views here.
# @api_view()
# def home(request):

#     return Response({'msg' : "hello world"})
#     # return HttpResponse(" i am working ")




# @api_view(["GET"])
# def home(request):
    
#     return Response({'msg' : "hello world"})
#     # return HttpResponse(" i am working ")





@api_view(["POST" , "GET"])
def home(request , id):
    bid = id # this is used when you test api in browserable drfś
    # print(request.data)

    if request.method == "GET":
        print(request.data ,"the data is came sa parse data ")
        id = request.data.get("id" , None )
        print(id)
        if id is not None :
            stu = Student.objects.get(pk=id)
            pd = StudentSerializer(stu)
            return Response(pd.data)


        # if id is not None:
        #     stu = Student.objects.get( request.data.get("id"))
        #     pd = StudentSerializer(stu)
        #     return Response(pd.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu , many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg = {
                'msg' : "data created",
                "data": serializer.validated_data
            }
            return Response(msg)
        return Response({"msg" : serializer.errors})
    
    
    return Response({'msg' : "hello world"})
    # return HttpResponse(" i am working ")