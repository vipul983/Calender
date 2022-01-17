from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from app.models import Meeting
from .forms import  CustomerRegistrationForm,MeetingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django_email_verification import send_email
# Create your views here.

def home(request):
    list=Meeting.objects.all()
    return render(request,'home.html',{'list': list})

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! You are registered successfully')
            # form.save()
            user = form.save( commit= False)
            user.is_active = False
            user.save()
            send_email(user)

        return render(request,'customerregistration.html',{'form':form})



    
def Deletemeet(request,pk):
    Meeting.objects.get(pk=pk).delete()
    list=Meeting.objects.all()
    return render(request,'home.html',{'list': list})




class AddMeetView(View):
    def get(self,request):
        form=MeetingForm()
        return render(request,'addmeet.html',{'form':form})
    def post(self,request):

        form=MeetingForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            description = request.POST.get('description')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            
            messages.success(request,'Hurray!! Meeting add successfully')
            meet = Meeting(title=title, description = description,start_time=start_time, end_time = end_time)
            meet.save()
        return render(request,'addmeet.html',{'form':form})



class EditMeetView(View):
    def get(self,request,pk):
        Meeting.objects.filter(pk=pk).delete()
        return redirect('/addmeet')


