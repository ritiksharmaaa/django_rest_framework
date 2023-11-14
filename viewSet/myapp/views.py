from django.shortcuts import render
from .models import Student 
from .serializer import StudentSerializer

from rest_framework import viewsets 
from rest_framework.response import Response 
from rest_framework import status 


# Create your views here.


class Student_data(viewsets.ViewSet):
    def list(self , request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu , many=True)
        return Response(serializer.data )
    def retrieve(self , request , pk=None):
        id = pk 
        if id is  not None :
            
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
    def create(self , request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "data created "} , status= status.HTTP_204_CREATED)
        return Response({'msg' : serializer.errors} , status=status.HTTP_400_BAD_REQUEST)
    
    def update(self , request ,pk):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'data updated'})
        return Response({serializer.errors},  status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self , request , pk):
        id = pk 
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : " data updated ! "})
        return Response({'msg'  : serializer.errors })

    def destroy(self , request , pk):
        id = pk 
        stu = Student.objects.get(id=id)
        stu.delete() 
        return Response({'msg' :  " data deleted "}) 
