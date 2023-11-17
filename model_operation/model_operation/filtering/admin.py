from django.contrib import admin
from .models import Student_data
# Register your models here.
@admin.register(Student_data)
class Student_dataAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name'  , 'last_name' , 'roll' , 'city' , 'passby']
    

