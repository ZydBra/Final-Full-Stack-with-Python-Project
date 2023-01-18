from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('user_account/', views.user_account, name='user_account'),
    path('logout/', views.user_logout, name='logout'),
    path('password_change/', views.password_change, name="password_change"),
]
