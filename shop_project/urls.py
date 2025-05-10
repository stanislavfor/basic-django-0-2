# shop_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),  # Маршруты shop приложения
    path('accounts/', include('django.contrib.auth.urls')),  # Стандартная URL-аутентификация
]