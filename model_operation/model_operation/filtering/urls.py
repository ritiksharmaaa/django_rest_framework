
from django.contrib import admin
from django.urls import path , include
from .views import StudentListApi


urlpatterns = [
    path("api/" , StudentListApi.as_view() , name="list-student")
]
