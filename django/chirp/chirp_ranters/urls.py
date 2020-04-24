from django.urls import path
from . import views

app_name = 'chirp_ranters' 
urlpatterns = [
    path('beseech', views.beseech, name='beseech'),
    path('user/<str:trollavatar>/', views.details, name='details'),
]