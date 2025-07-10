from django.urls import path
from app import views

urlpatterns = [
    # path("",views.blog_html),
    path('',views.index)
]