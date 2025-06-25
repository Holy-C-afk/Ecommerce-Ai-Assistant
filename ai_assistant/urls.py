from django.urls import path
from . import views

urlpatterns = [
    path('description/', views.description_generator, name='description_generator'),
    path('description/delete/<int:pk>/', views.delete_description, name='delete_description'),
    path('description/download/<int:pk>/', views.download_description, name='download_description'),
    path('description/regenerate/', views.regenerate_description, name='regenerate_description'),
] 