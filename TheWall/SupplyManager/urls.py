from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_page),
    path('confirm/', views.confirmation_page),
]
