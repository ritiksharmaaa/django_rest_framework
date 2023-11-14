from django.shortcuts import render
from rest_framework import viewsets
from .models import Student 
from .serializer import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser



# Create your views here.


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    authentication_classes = [BasicAuthentication] # we have to lot more after defining this ther perm allowy any 
    # permission_classes = [IsAuthenticated] # alos give more than one permisoon by comman , 
    permission_classes = [IsAdminUser] # ony is staff true only use it . 




















#  if you write more than one viewset or more class you have to define manauly for each time in each class . 

# so best way to do define this authentication globaly  - 

# write this code in setting .py 
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES' : ['rest_framework.authentication.BasicAuthentication'],
#     'DEFAULT_PERMISSION_CLASSES' : ['rest_framework.permissions.IsAuthenticated']
# }

# after define globaly if you want to not want globalyy so we have to overide also . to do custome or other permission .abs



