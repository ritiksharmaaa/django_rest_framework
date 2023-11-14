from django.shortcuts import render
from .models import Student 
from .serializer import StudentSerializer
from rest_framework import viewsets 
from rest_framework.authentication import BasicAuthentication , SessionAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser , AllowAny

# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    



