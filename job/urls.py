

from django.urls import path , include
from . import views  # " . " tis mean the views in the same path 

urlpatterns = [
    path('', views.job_list), # type: ignore
    path('<int:id>', views.job_details), # type: ignore
]
