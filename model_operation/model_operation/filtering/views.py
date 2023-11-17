from django.shortcuts import render
from .serializer import Student_Serializer 
from .models import Student_data

from rest_framework.generics import ListAPIView 

class StudentListApi(ListAPIView):
    queryset = Student_data.objects.all()
    # queryset = Student_data.objects.filter(passby="2023")
    serializer_class = Student_Serializer

    # def get_queryset(self):
    #     user = self.request.user 
    #     return Student_data.objects.filter(user=user)
    

