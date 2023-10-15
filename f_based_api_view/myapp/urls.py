from django.urls import path 
from . import views 
urlpatterns = [
    path("", views.home ,  name="test"),
    path("<int:id>/", views.home ,  name="test")
]
