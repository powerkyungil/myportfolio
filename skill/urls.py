from django.urls import path
from . import views

urlpatterns = [
    path('', views.skill_view, name='skill_view'),
]
