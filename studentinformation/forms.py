from django import forms

class StudentForms(forms.Form):
    
    student_first_name = forms.CharField(max_length= 200)
    student_last_name = forms.CharField(max_length=100)
    student_class = forms.CharField(max_length= 150)
    student_address = forms.CharField(max_length= 160)
    student_school = forms.CharField()
    student_email = forms.EmailField(max_length=100)
    
    