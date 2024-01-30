from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductView, basename='product')
router.register(r'categories', views.CategoryView, basename='category')

urlpatterns = [
    path('', include(router.urls))
]