
from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index,),
    path('upload/',views.upload,),
    path('exercise/',views.exercise,),
    path('blog/',views.blogpost,),
]