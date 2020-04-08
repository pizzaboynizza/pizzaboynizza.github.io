from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
    path('delete/', views.incomplete, name='incomplete'),
    path('detail/', views.detail, name='detail'),
    path('complete/', views.complete, name='complete'),
]