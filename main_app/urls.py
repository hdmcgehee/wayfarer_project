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
    
    
    # ___________    CITY SHOW    _________
    path('city/<int:city_id>', views.city_index, name = 'city_index'),

    # ___________    USER PROFILE  __________
    path('profile/', views.profile, name = 'profile'),

    # ___________    Post Show Page  __________
    path('post/<int:post_id>', views.post_detail, name = 'post_detail'),

    # ___________    Post Edit Page  __________
    path('post/<int:post_id>/edit', views.post_edit, name = 'post_edit'),

    # ___________    Post Delete Page  __________
    path('post/<int:post_id>/delete', views.post_delete, name = 'post_delete'),


]