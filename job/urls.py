

from django.urls import path , include
from . import views  # " . " tis mean the views in the same path 

urlpatterns = [
    path('', views.job_list),
    path('<int:id>', views.job_details),
]
