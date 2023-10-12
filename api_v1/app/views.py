from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from rest_framework.renderers import JSONRenderer
from  . serializer.serializer import studentSerializer 
from . models import myStudent 
# Create your views here.




def home(request):
    stu = myStudent.objects.all()
    print(stu)
    data = studentSerializer(stu , many=True)
    print(data)
    json_data = JSONRenderer().render(data.data)
    print(json_data)
    return JsonResponse(data.data , safe=False) #here safe false because when we serialize data for many it give list not dict so that why we need to give safe = false so it can  run 
    # return HttpResponse(json_data , content_type="application/json")

def home1(request , pk):
    stu = myStudent.objects.get(id=pk)
    print(stu)
    data = studentSerializer(stu)
    print(data)
    # if not want to write this two line you use json response 
    # json_data = JSONRenderer().render(data.data)
    # print(json_data)
    # return HttpResponse(json_data , content_type="application/json")

    # return render( request ,'home.html')
    # return HttpResponse (" i am working ")
    return JsonResponse(data.data , safe=True)

