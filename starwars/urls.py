from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='Welcome to End Star Wars'),
    path('havecourse/', views.havecourse, name='Have a Course to Swap?'),
    path('wantcourse/', views.wantcourse, name='Want to Swap a Course?'),
    path('addcourse/', views.addcourse, name='Adding a course'),
    path('selectcourse/', views.selectcourse, name='Selecting a course'),

    
]