from django.urls import path
from fourthApp import views

app_name = 'fourthApp'

urlpatterns = [
    path('relative/', views.relative, name="relative"),
    path('other/', views.other, name="other"),
]
