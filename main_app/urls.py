from django.urls import path
from . import views

urlpatterns = [
    
    
    # ___________    HOME      ____________
    path('home/', views.home, name='home'),


    # _____________  AUTH  _______________
    # ___________    SIGNUP      _________
    path('', views.signup, name='signup'),


    # ___________    CITY DETAIL    _________
    path('city/', views.city_detail, name = 'city_detail'),

    # ___________    USER PROFILE  __________
    path('profile/', views.profile, name = 'profile'),

]