from django.db import models

# Create your models here.

class StudentModel(models.Model):
    
    student_first_name = models.CharField(max_length= 200)
    student_last_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length= 150)
    student_address = models.CharField(max_length= 160)
    student_school = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100)
    slug = models.SlugField()
    
    def __str__(self):
        return self.student_first_name
    
    
class KidClasses (models.Model):
    class_name = models.CharField(max_length=100)
    content = models.TextField()
    age_of_kid = models.CharField(max_length=100)
    total_seat = models.CharField(max_length=100)
    class_time = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    
    def __str__(self) -> str:
        return self.class_name
    
class BlogPost (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    
    def __str__(self) -> str:
        return self.title
    
class Teachers (models.Model):
    teacher_name = models.CharField(max_length=100)
    teacher_subject = models.TextField()
    image = models.ImageField(upload_to='images')
    
    def __str__(self) -> str:
        return self.teacher_name