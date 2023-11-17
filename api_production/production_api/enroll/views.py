from django.shortcuts import render 
from django.contrib import messages 
from django.http import HttpResponseRedirect
from . forms import UserForm
from . models import User 
from django.views.generic.base import TemplateView , RedirectView
from django.views import View 
# Create your views here.
# print(User.objects.all())


class addshow_data(TemplateView):
    template_name ='enroll/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = UserForm() 
        stu = User.objects.all() 
        context = {'datas' : stu , 'form' : fm}
        return context
    def post(self,request):
        fm = UserForm(request.POST )
        if fm.is_valid():
            fm.save()
            messages.success(request , ' Student Add Successfuly ')
        return HttpResponseRedirect("/")


class delete_data(RedirectView):
    url="/"
    def get_redirect_url(self , *args , **kwargs):
        # print (kwargs['id'])
        del_id = kwargs['id']
        User.objects.get(id=del_id).delete()
        # messages.success(request , "Data is deleted ")
        return super().get_redirect_url(*args , **kwargs)


class Update_data(View):
    # we want two thing get data or change on post 
    def get (self , request , id): 
        # also write kwargs
        instance = User.objects.get(id=id)
        fm = UserForm(initial={'name' : instance.name , 'email' : instance.email , 'password' : instance.password })
        context ={
        'form' : fm ,
        }
        return render (request , 'enroll/update.html' , context)

    def post(self , request , id):
        instance = User.objects.get(id=id)
        fm = UserForm ( request.POST , instance=instance)
        if fm.is_valid():
            fm.save()
            messages.success(request , " Student data update succesfully ")
            return HttpResponseRedirect('/')




        



#for class base duse VIew 
# def Update_data(request , id ):
#     instance = User.objects.get(id=id)
#     if request.method == "POST":
#         fm = UserForm ( request.POST , instance=instance)
#         if fm.is_valid():
#             fm.save()
#             messages.success(request , " Student data update succesfully ")
#             return HttpResponseRedirect('/')
#     else:
#         fm = UserForm(initial={'name' : instance.name , 'email' : instance.email , 'password' : instance.password })
#     context ={
#         'form' : fm ,
#     }
#     return render (request , 'enroll/update.html' , context)


# def delete_data(request , id ):
#     data = User.objects.get(id=id)
#     data.delete()
#     messages.success(request , "Data is deleted ")
#     return HttpResponseRedirect("/")


# def addshow_data(request):
#     if request.method == "POST":
#         fm = UserForm(request.POST )
#         if fm.is_valid():
#             fm.save()
#             messages.success(request , ' Student Add Successfuly ')
#         return HttpResponseRedirect("/")
#     else:
#         fm = UserForm()
#     stu = User.objects.all()
#     context={
#         'form' : fm ,
#         'datas' : stu ,
#     }
#     return render (request, 'enroll/index.html' ,context )
