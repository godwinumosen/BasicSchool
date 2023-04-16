from django.contrib import admin
from .import models
from .models import StudentModel,KidClasses,BlogPost,Teachers
# Register your models here.


    
admin.site.register(StudentModel)
admin.site.register(KidClasses)
admin.site.register(BlogPost)
admin.site.register(Teachers)