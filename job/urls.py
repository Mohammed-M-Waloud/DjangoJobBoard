

from django.urls import path , include
from . import views  # " . " tis mean the views in the same path 
app_name = 'job'
urlpatterns = [
    path('', views.job_list),
    path('<str:slug>', views.job_details , name="job_details"),
]
