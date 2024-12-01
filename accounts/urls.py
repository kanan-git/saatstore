from django.urls import path

from accounts import views as account_views

urlpatterns = [
    path('register/', account_views.register, name='register'),
    path('login/', account_views.login, name='login'),
    path('profile/', account_views.profile, name='profile'),
    path('my_products/', account_views.my_products, name='my_products'),
    path('logout/', account_views.logout, name='logout')
]
