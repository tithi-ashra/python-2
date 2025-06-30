from django.contrib import admin
from django.urls import path
from fees import views

urlpatterns = [
    path('paydj/',views.pay_dj),
    path('paypy/',views.pay_python),
    path('payfsd/',views.pay_fsd),
]