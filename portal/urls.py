from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('fill-form/', views.fill_exam_form, name='fill_form'),
]