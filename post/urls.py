from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create_post),
    path('detail/<int:id>', views.detail_post),
    path('edit/<int:id>', views.edit_post),
    path('delete/<int:id>', views.delete_post)
]
