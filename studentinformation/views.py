from django.shortcuts import render,redirect
from .models import StudentModel,KidClasses,BlogPost,Teachers
# Create your views here.
from .forms import StudentForms

def home (request): 
    classes = KidClasses.objects.all()
    blogs = BlogPost.objects.all()
    title="New Approach to Kids Education"
    page="The education your child receives will set the groundwork for future successes. No matter his age -- from kindergarten to high school --we have all the advice and information you need on reaching potential in reading, writing, math, and more"
    
    context={'title':title,'page':page,'classes':classes,'blogs':blogs}
    return render(request,'home.html',context)

def register (request):
    form = StudentForms(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data['student_first_name']
        last_name = form.cleaned_data['student_last_name']
        clas = form.cleaned_data['student_class']
        address = form.cleaned_data['student_address']
        school = form.cleaned_data['student_school']
        email = form.cleaned_data['student_email']
        
        student = StudentModel(student_first_name = first_name,student_last_name=last_name,student_class=clas,student_address=address,student_school=school,student_email=email)
        student.save()
        return render(request,'ack.html',{'title':'Registered Successfully'})
        
    context={'form':form}
    return render(request,'register.html',context)


def existing(request):
    title = "All Registered Students"
    queryset = StudentModel.objects.all()
    context ={
        "title":title,
        "queryset":queryset,
    }
    return render(request,'existing.html',context)
    

def dropout (request):
    return render(request,'dropout.html',{})

def login(request):
    return render(request, 'login.html',{})

def search (request):
    return render (request, 'existing.html',{})

def teachers (request):
    head = "OUR TEACHERS"
    head_title = "MeeT Our Teachers"
    teachers = Teachers.objects.all()
    context ={'teachers':teachers,'head':head,'head_title':head_title}
    return render(request,'teachers.html',context)

def contact(request):
    return render(request, 'contact.html',{})