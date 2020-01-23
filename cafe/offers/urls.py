from django.urls import path
from . import views

urlpatterns = [
    path("", views.offers),
    path("<str:name>/",views.offercategory)
    
    
    ]
