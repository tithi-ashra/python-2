from django.urls import path
from home import views

urlpatterns = [
    path('',views.home),
    path('html/',views.home_html),
    path('html1/',views.home_html1),
    path('html2/',views.home_html2,name='tithi'),
]