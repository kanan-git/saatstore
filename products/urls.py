from django.urls import path

from products import views as products_view

urlpatterns = [
    path('', products_view.landpage, name='landpage'),
    path('details/', products_view.details, name='details'),
    path('buy/', products_view.buy, name='buy'),
    path('add_new/', products_view.add_product, name='add'),
    path('edit_product/', products_view.edit_product, name='edit'),
    # path('remove/', products_view.remove_product, name='remove')
]
