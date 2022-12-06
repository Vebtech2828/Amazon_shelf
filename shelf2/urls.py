from django.urls import path
from shelf2 import views

urlpatterns = [
    path('first/', views.first_view),
    path('second/', views.second_view),
    path('third/', views.third_view),
    path('fourth/', views.fourth_view),
    path('fifth/', views.fifth_view),
]
