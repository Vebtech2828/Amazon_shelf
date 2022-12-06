from django.urls import path
# from shelf1 import views
from . import views

urlpatterns = [
    path('home/', views.headline),
    path('time/', views.headline),
    path('welcome/', views.wish),
]