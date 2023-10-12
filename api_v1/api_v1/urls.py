"""
URL configuration for api_v1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views 
from deserialization import views as d
from crud import views as crud
urlpatterns = [
    path('admin/', admin.site.urls),
    path('serializer' , views.home , name="v1 serializer data to json "),
    path('serializer/<int:pk>/' , views.home1 , name=" v1 serialize data with pk id "),

    #  d-serializations 

    path("d-serial/", d.home ,  name="decerialization "),
    path("crud/", crud.home ,  name="decerialization "),
]
