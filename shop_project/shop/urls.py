"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from django.contrib import admin
from .views import home_page, AddProduct, EditProduct, DeleteProduct, AddOrder, EditOrder, DeleteOrder, update_profile
from django.urls import include
from .views import clients_list
from .views import products_list
from .views import orders_list
from .views import client_detail
from .views import product_detail
from .views import order_detail
from .views import add_client
from .views import update_order
from .views import add_product
from .views import delete_product
from .views import products_total

urlpatterns = [
    path('admin/', admin.site.urls),  # Панель администратора
    path('', home_page, name='home'),              # Главное правило для корня сайта
    path('add-product/', add_product, name='add_product'),
    path('edit-product/<int:pk>/', EditProduct.as_view(), name='edit_product'),
    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),
    # path('delete-product/<int:pk>/', DeleteProduct.as_view(), name='delete_product'),
    path('add-order/', AddOrder.as_view(), name='add_order'),
    path('edit-order/<int:pk>/', EditOrder.as_view(), name='edit_order'),
    path('delete-order/<int:pk>/', DeleteOrder.as_view(), name='delete_order'),
    path('update-profile/', update_profile, name='update_profile'),
    path('accounts/', include('django.contrib.auth.urls')),  # Стандартная URL-аутентификация
    path('clients/', clients_list, name='clients_list'),
    path('products/', products_list, name='products_list'),
    path('products-total/', products_total, name='products_total'),
    path('orders/', orders_list, name='orders_list'),
    path('clients/<int:client_id>/', client_detail, name='client_detail'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),
    path('add-client/', add_client, name='add_client'),
    path('update-order/<int:order_id>/', update_order, name='update_order'),

]