from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
]
