from django.urls import path
from . import views

urlpatterns = [
    
    # __________________    SIGNUP        _________________
    path('', views.signup, name='signup'),


    # __________________    USER PROFILE  _________________
    path('profile/<int:profile_id>', views.profile, name = 'profile'),

    path('profile/', views.user_profile, name = 'user_profile'),



    # __________________    CITY INDEX    _________________
    path('city/<int:city_id>', views.city_index, name = 'city_index'),
    



    # __________________    POST DETAIL   _________________
    path('post/<int:post_id>', views.post_detail, name = 'post_detail'),

    # __________________    POST Edit     _________________
    path('post/<int:post_id>/edit', views.post_edit, name = 'post_edit'),

    # __________________    POST DELETE   _________________
    path('post/<int:post_id>/delete', views.post_delete, name = 'post_delete'),

]