from django.urls import path
from details import views

urlpatterns = [
    path("",views.learn_details)
]