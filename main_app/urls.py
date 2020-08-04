from django.urls import path
from . import views

urlpatterns = [
    
    
    # ___________    HOME      ____________
    path('', views.home, name='home'),


    # ___________    CITY DETAIL    _________
    path('city/', views.city_detail, name = 'city_detail')

]