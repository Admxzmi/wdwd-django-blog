from django.urls import path

from . import views

urlpatterns = [
    # Home page
    path('home/', views.index, name='index'),
]
