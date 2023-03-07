from django.urls import path
from . import views

urlpatterns = [
    path('main/',views.mainPage, name='mainPage'),
    #path('photos/<str:pk>/', views.viewPhoto,name='photo'),
    path('login/',views.login, name='login'),
    path('',views.home, name='home'),
]