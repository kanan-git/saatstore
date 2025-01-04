from django.urls import path

from accounts import views as account_views

urlpatterns = [
    path('login/', account_views.login, name='login'),
    path('register/', account_views.register, name='register'),
    path('profile/', account_views.profile, name='profile'),
    path('dashboard/', account_views.dashboard, name='dashboard'),
    path('logout/', account_views.logout, name='logout')
]
