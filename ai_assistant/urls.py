from django.urls import path
from . import views

urlpatterns = [
    path('description/', views.description_generator, name='description_generator'),
] 