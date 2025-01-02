from django.urls import path

from products import views as products_view

urlpatterns = [
    path('', products_view.landpage, name='landpage'),
    path('products/', products_view.all_products, name='products_list'),
    path('add_new/', products_view.add_product, name='add'),
    path('details/<int:id>/', products_view.details, name='details'),
    path('buy/<int:pk>', products_view.buy, name='buy'),
    path('edit_product/<int:pk>', products_view.edit_product, name='edit'),
    path('remove_product/<int:pk>', products_view.remove_product, name='remove')
]
