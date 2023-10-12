from django.contrib import admin
from .models import myStudent 

# Register your models here.


@admin.register(myStudent)
class myStudentAdmin(admin.ModelAdmin):
    list_display  =  [ 'id', 'name' , 'roll' , 'city']