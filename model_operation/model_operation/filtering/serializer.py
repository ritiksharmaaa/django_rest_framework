# from rest_framework import 
from .models import Student_data 
from rest_framework import serializers

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_data
        fields = ['name' , 'last_name' , 'roll' ,'city' , 'passby']