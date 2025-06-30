from django.contrib import admin
from django.urls import path
from course import views

urlpatterns = [
    path('',views.learn_html),
    path('l/',views.learn_dj),
    path('p/',views.learn_python),
    path('f/',views.learn_fsd),
]