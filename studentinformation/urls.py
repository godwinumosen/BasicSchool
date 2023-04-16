from django.urls import path
from . import views

app_name = 'studentinformation'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('teachers', views.teachers, name='teachers'),
    path('register',views.register, name='register'),
    path('existing',views.existing, name='existing'),
    path('dropout',views.dropout, name='dropout'),
    path('login',views.login, name='login'),
    path('search',views.search, name='search'),
    path('contact',views.contact, name='contact'),
]