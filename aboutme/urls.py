from django.urls import path
from . import views

urlpatterns = [
    path('', views.aboutme_view, name='aboutme_view'),
]
