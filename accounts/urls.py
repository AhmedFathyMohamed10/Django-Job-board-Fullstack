from django.urls import path
from . import views


urlpatterns = [
    path('sign-up', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='edit_profile'),
    path('profile/edit/user', views.user_edit, name='user_edit'),
]
