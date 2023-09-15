from django.urls import path, include
from .views import index, ProductView
from rest_framework import routers

router =  routers.DefaultRouter()

router.register(r'product', ProductView, 'product')

urlpatterns = [
    path('', index, name = "index"),
    path('api/', include(router.urls))
]
