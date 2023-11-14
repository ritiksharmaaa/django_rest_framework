from django.shortcuts import render
from .models import Student 
from .serializer import StudentSerializer
from rest_framework import viewsets 
from rest_framework.authentication import BasicAuthentication , SessionAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser

# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes =[SessionAuthentication]
    permission_classes = [IsAuthenticated]# you can give more permmsion  same as tutorial 
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdmin] 
    # permission_classes = [IsAuthenticationOrReadOnly]
    # permission_classes = [DjangoModelPermissionOrAnonReadOnly]



