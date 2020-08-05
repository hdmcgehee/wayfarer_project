from django.urls import path
from . import views

urlpatterns = [
    
    
    # ___________    HOME      ____________
    path('', views.home, name='home'),


    # ___________    SIGNUP      ____________
    path('', views.home, name='signup'),


    # ___________    CITY DETAIL    _________
    path('city/', views.city_detail, name = 'city_detail')

]